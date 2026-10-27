# Excerpt from the private Sharpenly pipeline; trimmed for readability.
#
# What this shows: every generated question passes a rule-based gate before a
# human sees it. The gate returns one of three verdicts:
#   accept  - structurally sound, judgment-based, grounded, not a clone
#   review  - good question with a fixable flaw (for example a length tell)
#   reject  - broken, trivia, off-topic, or a near-duplicate
# A separate check decides whether a whole generation run was a product success.

import re
import numpy as np

DEDUP_COSINE = 0.90  # generation-time near-duplicate threshold (MiniLM embeddings)

# Bare numbers or specs as the answer are lookup trivia, not judgment.
BARE_NUMBER = re.compile(
    r"^\s*\d+(\.\d+)?\s*(-\s*\d+)?\s*(volts?|v|amps?|a|ohms?|psi|ft-?lbs?|nm|mm|in|%|rpm)?\s*$", re.I)

# Stems that ask the learner to recall a statistic or a quoted word.
RECALL_STEM = re.compile(
    r"what percentage|what percent|how many .{0,30}(said|reported|responded)|"
    r"what (word|term|phrase)\b|qu[eé] porcentaje|qu[eé] (palabra|t[eé]rmino)", re.I)

# Academic theory that does not belong in shop-floor training.
ACADEMIC = re.compile(r"\b(slip angle|hysteresis|durometer|coefficient of friction)\b", re.I)


def structural_errors(q):
    """Simplified stand-in for the structural validator: 4 distinct choices per
    language, correct answer present in both languages at the same index."""
    errs = []
    for lang in ("en", "es"):
        choices = q.get(f"choices_{lang}", [])
        if len(choices) != 4 or len(set(choices)) != 4:
            errs.append(f"{lang}: need 4 distinct choices")
        if q.get(f"correct_answer_{lang}") not in choices:
            errs.append(f"{lang}: correct answer not in choices")
    if not errs and (q["choices_en"].index(q["correct_answer_en"])
                     != q["choices_es"].index(q["correct_answer_es"])):
        errs.append("EN/ES correct index mismatch")
    return errs


def _length_tell(choices, correct):
    """A real tell only if the correct answer is >30% AND >=12 chars longer (or
    shorter) than the other choices. A flat character rule false-rejects
    sentence-length scenario answers, so the check is proportional."""
    others = [len(c) for c in choices if c != correct]
    if not others or not correct:
        return None
    n, longest, shortest = len(correct), max(others), min(others)
    if n > longest * 1.30 and n - longest >= 12:
        return "correct dominates length (giveaway)"
    if n < shortest * 0.70 and shortest - n >= 12:
        return "correct too short (giveaway)"
    return None


def gate(q, existing_emb, accepted_emb, embed):
    """Return (verdict, tier, notes). verdict in {accept, review, reject}.
    HARD failures reject. SOFT failures route to a human reviewer."""
    hard = structural_errors(q)
    if BARE_NUMBER.match(q.get("correct_answer_en", "")):
        hard.append("trivia: bare-number answer")
    stem = q.get("question_en", "") + " || " + q.get("question_es", "")
    if RECALL_STEM.search(stem):
        hard.append("trivia: recall-of-statistic/word stem (not judgment)")
    if ACADEMIC.search(stem):
        hard.append("academic theory, not shop-relevant")

    # Near-duplicate check against the existing bank and against items
    # already accepted in this run (cosine on normalized embeddings).
    e = embed(q["question_en"])
    sim_bank = float(np.max(existing_emb @ e)) if len(existing_emb) else 0.0
    sim_run = float(np.max(np.stack(accepted_emb) @ e)) if accepted_emb else 0.0
    if max(sim_bank, sim_run) >= DEDUP_COSINE:
        hard.append(f"semantic clone (cos {max(sim_bank, sim_run):.2f})")
    if hard:
        return "reject", "reject", hard

    # Soft flags: a good question that needs a small fix before it ships.
    soft = []
    for lang in ("en", "es"):
        tell = _length_tell(q[f"choices_{lang}"], q[f"correct_answer_{lang}"])
        if tell:
            soft.append(f"{lang.upper()} {tell} - balance choice lengths")
    grounded = bool(q.get("source"))   # cites a retrieved passage
    scenario = bool(q.get("is_scenario"))
    self_rating = q.get("self_rating", "review")
    if soft or self_rating == "reject":
        return "review", "review", (soft or ["model self-flagged for a human eye"])
    if self_rating == "gold" and scenario and grounded:
        return "accept", "gold", []
    if self_rating in ("gold", "practice") and grounded:
        return "accept", "practice", ([] if scenario else ["not a scenario"])
    return "review", "review", ["needs human eye"]


def product_success(parsed_count, accepted_count, requested_count, stop_reasons):
    """A run counts as a success only if the output parsed, the count is
    reasonable, and questions survived the gate. API 'succeeded' alone is not
    success. Returns (ok, reason)."""
    truncated = sum(s == "max_tokens" for s in stop_reasons)
    if truncated:
        return False, f"{truncated} requests hit max_tokens (truncated)"
    if parsed_count == 0:
        return False, "0 questions parsed"
    if requested_count and parsed_count < 0.8 * requested_count:
        return False, f"only {parsed_count}/{requested_count} parsed (<80%)"
    if accepted_count == 0:
        return False, "0 accepted after gates"
    return True, "parsed + gated + accepted OK"
