# Postmortem: 617 of 617 requests "succeeded" and 0 questions were usable

## Summary

A batch generation run finished with status "succeeded" on all 617 requests. It produced zero usable questions. Every response hit the output-token limit and was cut off before the structured JSON closed, so nothing parsed.

## What happened

- Every request ended with `stop_reason = max_tokens`.
- The structured output was truncated mid-object, so the parser got nothing. Roughly 4.9M output tokens were generated and none could be recovered.
- At the API level the run looked fine. For the product it was a total loss.

## The numbers

| Item | Value |
|---|---|
| Requests | 617 |
| Output cap per request | 8,000 tokens |
| Questions requested per request | 20 |
| Measured size of one bilingual question | about 700 tokens |
| Output needed per request | about 14,000 tokens |
| Needed versus cap | about 175% |

A fully bilingual item is large: two question strings, eight choice strings, two explanations, a usefulness line, and a self-rating. Twenty of them could not fit under the cap. Truncation was certain.

## Why the pilots did not catch it

- The earlier pilots used 8 or fewer questions per request, which fit under the cap.
- The format check used 3 questions per request, which also fit.
- Format, parser, and quality all looked correct. None of them ran at the real request size.

Lesson: validate the request size, not only the request format.

## Rules added

1. Never submit a large batch without a real-size proof request first.
2. API "succeeded" is not success. Product success means parseable, usable output.
3. `stop_reason == max_tokens` fails the run.
4. Zero parsed questions fails the run.
5. Truncated output fails the run.
6. If estimated output per request is above 70% of the cap, block before running.
7. If the cost estimate is missing, block.
8. If the parser was not tested at the batch's request size, block.
9. If a small real mini-batch fails, block the full batch.
10. No full run without a written preflight report.

## What enforces them now

- **Preflight calculator.** Blocks any config where estimated output per request exceeds 70% of the cap. The old config (20 questions, 8,000 cap) sits at 175% and is blocked. The new config (10 questions, 12,000 cap) sits at 58% and passes.
- **Real-size proof.** One request at the exact batch size. It must not hit `max_tokens` and must parse the expected count.
- **Mini-batch proof.** A tiny real batch must parse with zero truncations before the full batch is allowed.
- **Product-success gate.** See `product_success()` in [gate_excerpt.py](gate_excerpt.py).
- **Config fix.** Questions per request went from 20 to 10. Output cap went from 8,000 to 12,000.

## Result

The corrected pipeline ran a full batch of 11,870 parsed questions. 10,356 passed the gate, 451 went to human review, and 1,063 were rejected.
