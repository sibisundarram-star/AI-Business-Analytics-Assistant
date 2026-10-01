def generate_insights(chart_df, x, y, aggregation):

    question = question.lower()

    if chart_df.empty:
        return "No data available."

    highest = chart_df.loc[chart_df[y].idxmax()]
    lowest = chart_df.loc[chart_df[y].idxmin()]

    # ------------------------
    # Average
    # ------------------------
    if aggregation == "mean":

        return (
            f"💡 **{highest[x]}** has the highest average "
            f"**{y}** ({highest[y]:,.2f})."
        )

    # ------------------------
    # Count
    # ------------------------
    if aggregation == "count":

        return (
            f"💡 **{highest[x]}** has the highest count "
            f"({highest[y]:,.0f})."
        )

    # ------------------------
    # Sum / Revenue / Sales
    # ------------------------

    total = chart_df[y].sum()

    top2 = chart_df.nlargest(2, y)

    top = top2.iloc[0]

    share = (top[y] / total) * 100

    if len(top2) > 1:

        second = top2.iloc[1]

        diff = ((top[y] - second[y]) / second[y]) * 100

        return (
            f"💡 **{top[x]}** generated the highest **{y}** "
            f"({top[y]:,.2f}).\n\n"
            f"It contributed **{share:.1f}%** of the total "
            f"and performed **{diff:.1f}%** better than "
            f"**{second[x]}**."
        )

    return (
        f"💡 **{top[x]}** contributed "
        f"**{share:.1f}%** of the total **{y}**."
    )