# Question quality rubric

Every accepted question must meet all of these. The automated gate enforces what a rule can check. A human reviewer covers the rest.

## Content

| # | Rule | Checked by |
|---|---|---|
| 1 | Useful in a real shop or workplace. | Prompt, human review |
| 2 | Role-specific. A service-advisor item is not a generic textbook item. | Role-filtered retrieval, human review |
| 3 | Tests judgment, not memory. Asks for the best next step, best response, best diagnosis direction, mistake to avoid, or best explanation to the customer. | Recall-stem patterns, human review |
| 4 | No statistic, percentage, research finding, or quoted word as the thing being tested. | Recall-stem patterns |
| 5 | No bare-number or spec answer that a person would look up. | Bare-number check, all-numeric-choices check |
| 6 | No academic or engineering theory unless the track is explicitly advanced. | Theory term list |
| 7 | Not a clone of an existing question. | Embedding similarity |
| 8 | Grounded: cites the retrieved passage it came from. | Source-field check |

## Choices

| # | Rule | Checked by |
|---|---|---|
| 9 | Exactly 4 choices per language, all distinct. | Structural validator |
| 10 | Distractors are real misconceptions that workers hold, not obvious-wrong filler. | Prompt, human review |
| 11 | No "all of the above" or "none of the above". No lazy "always" or "never". | Banned-pattern check |
| 12 | No answer-length giveaway. The correct answer is not noticeably longer or shorter than the others. Proportional rule: more than 30% and at least 12 characters off the other choices is flagged. | Length-tell check |

## Bilingual

| # | Rule | Checked by |
|---|---|---|
| 13 | Every question, choice, and explanation exists in English and Spanish. | Structural validator |
| 14 | Spanish is natural Mexican and Latin American register, not a literal translation. Formal "usted" for customer-facing and manager situations. | Prompt, human review |
| 15 | English and Spanish choices are aligned by position. The correct answer sits at the same index in both. | Structural validator |

## Scenario minimums

Scenario questions put the learner in a concrete situation: a customer or vehicle shows a symptom, a reading comes back, a person says something, and the question asks what to do.

| Track | Minimum share of scenario questions |
|---|---|
| Mechanic | 60% |
| Diagnostics | 60% |
| Tire tech | 60% |
| Service advisor | 75% |
| Management | 80% |
| Pro skills | 80% |

The minimum is stated in the generation prompt. Each review packet reports the actual share per role.

## Verdicts

| Verdict | When |
|---|---|
| Accept | All hard rules pass, no soft flags, grounded. Tier is gold if it is also a scenario, otherwise practice. |
| Review | Hard rules pass, but a soft flag applies, such as a length tell. A human fixes or declines it. |
| Reject | Any hard rule fails. The reason is recorded. |

## Level structure

Each normal track has exactly 8 difficulty levels. As the bank grows, questions are added inside those 8 levels. A level is a pool the app samples from, so a bigger pool means more replay value without changing the structure.
