import re

def detect_comparison(question):

    question = question.lower()

    if "compare" not in question and " vs " not in question:
        return None

    # compare A and B
    m = re.search(r"compare (.+?) and (.+)", question)

    if m:
        return (
            m.group(1).strip(),
            m.group(2).strip()
        )

    # A vs B
    m = re.search(r"(.+?)\s+vs\s+(.+)", question)

    if m:
        return (
            m.group(1).strip(),
            m.group(2).strip()
        )

    return None