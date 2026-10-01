def detect_ranking(question):

    question = question.lower()

    import re

    top = re.search(r"top\s+(\d+)", question)
    if top:
        return ("top", int(top.group(1)))

    bottom = re.search(r"bottom\s+(\d+)", question)
    if bottom:
        return ("bottom", int(bottom.group(1)))

    return None