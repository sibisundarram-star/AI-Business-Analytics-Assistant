def merge_query(current_query, last_query):

    current = current_query.lower().strip()

    followups = [
        "only",
        "compare",
        "and",
        "vs",
        "monthly",
        "yearly",
        "daily",
        "quarterly",
        "trend",
        "filter"
    ]

    # Only merge if the new query is actually a follow-up
    if last_query and any(current.startswith(word) for word in followups):
        return last_query + " " + current

    # Otherwise treat it as a brand-new question
    return current_query