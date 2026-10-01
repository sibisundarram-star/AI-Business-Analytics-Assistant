def aggregate_data(df, x, y, question, top_n=None, bottom_n=None):

    question = question.lower()

    # ---------- AVERAGE ----------
    if any(word in question for word in [
        "average", "avg", "mean"
    ]):
        result = df.groupby(x)[y].mean().reset_index()

    # ---------- MAX ----------
    elif any(word in question for word in [
        "maximum", "max", "highest"
    ]):
        result = df.groupby(x)[y].max().reset_index()

    # ---------- MIN ----------
    elif any(word in question for word in [
        "minimum", "min", "lowest"
    ]):
        result = df.groupby(x)[y].min().reset_index()

    # ---------- COUNT ----------
    elif any(word in question for word in [
        "count", "number of", "how many"
    ]):
        if x == y:
            result = (
                df.groupby(x)
                .size()
                .reset_index(name="Count")
            )
            y = "Count"

        else:
            result = (
                df.groupby(x)[y]
                .count()
                .reset_index()
            )

    # ---------- DEFAULT = SUM ----------
    else:
        result = (
            df.groupby(x)[y]
            .sum()
            .reset_index()
        )

    # ---------- TOP ----------
    if top_n:
        result = result.nlargest(top_n, y)

    # ---------- BOTTOM ----------
    if bottom_n:
        result = result.nsmallest(bottom_n, y)

    return result