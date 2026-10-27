# Excerpt from the private Sharpenly pipeline; trimmed for readability.
#
# Bilingual validation for the question bank. Every question carries English
# and Spanish text. The two must line up exactly, or a learner who switches
# language mid-quiz sees a different "correct" answer.

BANNED_PATTERNS = [
    "all of the above", "none of the above", "both a and b",
    "todas las anteriores", "ninguna de las anteriores",
]
REQUIRED = ("question_en", "question_es", "choices_en", "choices_es",
            "correct_answer_en", "correct_answer_es",
            "explanation_en", "explanation_es", "difficulty")


def validate_question(q, idx, role, level):
    errs, tag = [], f"{role} L{level} #{idx}"

    for field in REQUIRED:
        if not q.get(field):
            errs.append(f"{tag}: missing field '{field}'")
    if errs:
        return errs

    # 4 distinct choices per language.
    for lang in ("en", "es"):
        choices = q[f"choices_{lang}"]
        if len(choices) != 4:
            errs.append(f"{tag}: choices_{lang} has {len(choices)} entries, need 4")
        if len(set(choices)) != len(choices):
            errs.append(f"{tag}: choices_{lang} are not distinct")
        if q[f"correct_answer_{lang}"] not in choices:
            errs.append(f"{tag}: correct_answer_{lang} not in choices_{lang}")

    # EN/ES alignment: the correct answer sits at the same index in both.
    if not errs:
        i_en = q["choices_en"].index(q["correct_answer_en"])
        i_es = q["choices_es"].index(q["correct_answer_es"])
        if i_en != i_es:
            errs.append(f"{tag}: correct index differs (EN {i_en} vs ES {i_es})")

    # Banned distractor patterns, in both languages.
    for lang in ("en", "es"):
        for c in q[f"choices_{lang}"]:
            if any(p in c.lower() for p in BANNED_PATTERNS):
                errs.append(f"{tag}: banned distractor pattern in {lang}: {c[:40]!r}")

    # The correct answer must not be the longest or shortest choice (EN and ES).
    for lang in ("en", "es"):
        lengths = [len(c) for c in q[f"choices_{lang}"]]
        n = len(q[f"correct_answer_{lang}"])
        if n == max(lengths) and lengths.count(n) == 1:
            errs.append(f"{tag}: correct answer is the longest choice ({lang})")
        if n == min(lengths) and lengths.count(n) == 1:
            errs.append(f"{tag}: correct answer is the shortest choice ({lang})")
    return errs
