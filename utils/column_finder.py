from difflib import SequenceMatcher


def clean(text):
    return (
        text.lower()
        .replace("_", " ")
        .replace("-", " ")
        .replace(".", " ")
    )


def find_best_column(question, schema):

    question = clean(question)

    candidates = schema["dimensions"] + schema["metrics"]

    best_col = None
    best_score = 0

    words = question.split()

    for col in candidates:

        col_clean = clean(col)

        # Exact match
        if col_clean in question:
            return col

        # Match individual words
        for word in words:

            score = SequenceMatcher(
                None,
                word,
                col_clean
            ).ratio()

            if score > best_score:
                best_score = score
                best_col = col

    if best_score > 0.55:
        return best_col

    return None