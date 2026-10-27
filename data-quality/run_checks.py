# Runnable demo: apply the bilingual validator and the length-tell rule to the
# 20 sample questions in samples/questions_sample.json.
#
#   python data-quality/run_checks.py
#
# Standard library only. Exit code 1 if any hard check fails.

import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from validators_excerpt import validate_question  # noqa: E402


def length_tell(choices, correct):
    """Same proportional rule as _length_tell() in gate_excerpt.py."""
    others = [len(c) for c in choices if c != correct]
    if not others or not correct:
        return None
    n, longest, shortest = len(correct), max(others), min(others)
    if n > longest * 1.30 and n - longest >= 12:
        return "correct dominates length (giveaway)"
    if n < shortest * 0.70 and shortest - n >= 12:
        return "correct too short (giveaway)"
    return None


def to_bank_format(s):
    """The samples are stored as {en, es} pairs with one correct_index; the bank
    (and the validator) use flat *_en / *_es fields."""
    q = {"difficulty": s.get("difficulty"), "role": s.get("role"), "level": s.get("level")}
    for lang in ("en", "es"):
        q[f"question_{lang}"] = s["question"][lang]
        q[f"choices_{lang}"] = s["choices"][lang]
        q[f"correct_answer_{lang}"] = s["choices"][lang][s["correct_index"]]
        q[f"explanation_{lang}"] = s["explanation"][lang]
    return q


def main():
    samples = json.loads((HERE / "samples" / "questions_sample.json").read_text(encoding="utf-8"))
    questions = [to_bank_format(s) for s in samples]
    hard, soft = [], []
    for i, q in enumerate(questions):
        role, level = q.get("role", "?"), q.get("level", "?")
        # Hard errors: structure, EN/ES alignment, banned patterns.
        # The strict longest/shortest notes from the validator are reported as soft flags.
        for err in validate_question(q, i, role, level):
            (soft if "longest" in err or "shortest" in err else hard).append(err)
        for lang in ("en", "es"):
            tell = length_tell(q[f"choices_{lang}"], q[f"correct_answer_{lang}"])
            if tell:
                hard.append(f"{role} L{level} #{i}: {tell} ({lang})")

    print(f"Checked {len(questions)} bilingual questions")
    print(f"  hard failures (structure, EN/ES alignment, banned patterns, proportional length tell): {len(hard)}")
    print(f"  strict longest/shortest flags: {len(soft)}")
    print("  The strict rule flags most sentence-length scenario answers; the proportional")
    print("  rule only fires on a real giveaway. That gap is why the gate uses the proportional one.")
    for line in hard:
        print("  FAIL", line)
    for line in soft:
        print("  FLAG", line)
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
