# Data-quality case study: gating AI-generated bilingual training questions

I built a pipeline that generates training questions with an LLM and then refuses most of them until they pass a written rubric. This page covers the problem, the rubric, the gate, the measured results, one costly failure, and what I would do next.

## The problem

LLM-written quiz questions look fine at a glance. At scale they fail in quiet ways:

- The correct answer is the longest option, so test-takers guess it without knowing the topic.
- The question asks for a statistic or a quoted word, which tests memory of a source, not judgment.
- Distractors are obviously wrong, so the question teaches nothing.
- Near-duplicates inflate the bank without adding coverage.
- The Spanish is a literal translation, or the correct answer sits at a different position than in English.

The audience is shop technicians, service advisors, and managers. A wrong or silly question costs trust fast.

## The rubric

Full text in [RUBRIC.md](RUBRIC.md). In short, every accepted question must be useful in real work, role-specific, judgment-based, bilingual with aligned answers, and free of length tells. Scenario questions have per-role minimums.

## The gate

Code excerpts: [gate_excerpt.py](gate_excerpt.py) and [validators_excerpt.py](validators_excerpt.py).

Each generated item gets one of three verdicts:

| Verdict | Meaning | Examples |
|---|---|---|
| Accept | Meets the rubric | Grounded, judgment-based, no length tell |
| Review | Good item, fixable flaw, goes to a human | Correct answer much longer than the rest |
| Reject | Unusable | Broken structure, trivia stem, bare-number answer, near-duplicate |

Rejections keep a reason string. That makes the gate auditable: I can count why items fail and fix the prompt, not just the item.

Near-duplicate checks use MiniLM embeddings. The generation gate rejects at cosine similarity 0.90 or above, against both the existing bank and items already accepted in the same run. A separate audit of the finished bank flags clones at 0.92 or above.

## Iteration results

| Stage | Generated | Accepted | To human review | Rejected | Accept rate |
|---|---|---|---|---|---|
| Pilot (first prompt) | 50 | 7 | 0 | 43 | 14% |
| Repilot (tightened prompt and gate) | 25 | 21 | 4 | 0 | 84% |
| Full batch | 11,870 | 10,356 | 451 | 1,063 | 87% |

What changed between pilot and repilot:

- The prompt now states the rules the gate enforces: judgment over recall, equal-length choices, real misconceptions as distractors, shop-relevant only.
- The gate got proportional length-tell logic. A flat character rule rejected almost everything that had sentence-length answers.
- Length tells became a "review" verdict, not a reject. A good question with an unbalanced option is worth a human fix.

Cost per kept item fell about 4.4x from pilot to repilot.

Caveat: the repilot was smaller and aimed at roles that had failed before, so it is not a like-for-like comparison with the pilot. The full batch is the better estimate of steady-state quality.

### Full batch by role

| Role | Generated | Accepted | Review | Rejected | Accept rate |
|---|---|---|---|---|---|
| Mechanic | 2,500 | 1,975 | 94 | 431 | 79% |
| Diagnostics | 1,780 | 1,488 | 50 | 242 | 84% |
| Tire tech | 1,450 | 1,215 | 52 | 183 | 84% |
| Service advisor | 2,130 | 1,930 | 117 | 83 | 91% |
| Management | 1,530 | 1,450 | 40 | 40 | 95% |
| Pro skills: leadership | 1,250 | 1,195 | 37 | 18 | 96% |
| Pro skills: communication | 1,230 | 1,103 | 61 | 66 | 90% |

Technical roles reject more than the soft-skill roles. I have not broken the rejections down by rule per role, so I do not claim a cause. 36 of 1,233 batch requests errored and were excluded from these counts.

"Accepted" means the automated gate passed the item. It is not a claim about accuracy, and I have not measured agreement between the gate and human judges.

## The failure that shaped the rules

A batch once reported 617 of 617 requests succeeded and produced zero usable questions. Every response was cut off mid-output. Read the full write-up in [POSTMORTEM.md](POSTMORTEM.md). The rule that came out of it: **product success, not API success.** A run passes only if the output parsed, the count is reasonable, and questions survived the gate.

## Samples

[samples/questions_sample.json](samples/questions_sample.json) has 20 real questions from the shipped bank. They cover 7 roles and all 8 levels, in English and Spanish, scenario style. Source citations are removed.

For scale: 11,324 of the 16,887 non-exam questions in the bank (67%) are tagged scenario-based.

## What I would do next

1. Judge-versus-human agreement study. Have two or more human annotators label a random sample as accept, review, or reject. Compute inter-annotator agreement first, then gate-versus-human agreement, per rule. This turns "the gate passed it" into a measured number.
2. Add an LLM judge as a second pass for the rules regex cannot see: distractor plausibility and Spanish naturalness. Calibrate it against the human labels before trusting it.
3. Track per-rule rejection rates over time so a prompt change that shifts quality shows up in the data.
4. Add a native-speaker Spanish review sample for each new batch.
