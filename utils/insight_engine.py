import pandas as pd


def generate_business_insight(chart_df, x, y, question):

    if chart_df.empty:
        return "No insights available."

    highest = chart_df.loc[chart_df[y].idxmax()]
    lowest = chart_df.loc[chart_df[y].idxmin()]

    total = chart_df[y].sum()

    highest_pct = (
        highest[y] / total * 100
        if total != 0 else 0
    )

    insight = []

    insight.append(
        f"📈 **{highest[x]}** generated the highest **{y}** "
        f"(${highest[y]:,.2f})."
    )

    insight.append(
        f"📉 **{lowest[x]}** recorded the lowest **{y}** "
        f"(${lowest[y]:,.2f})."
    )

    insight.append(
        f"📊 The leading category contributes "
        f"**{highest_pct:.1f}%** of the displayed total."
    )

    if len(chart_df) > 5:

        top5 = chart_df.nlargest(5, y)

        concentration = top5[y].sum() / total * 100

        insight.append(
            f"🎯 The Top 5 account for "
            f"**{concentration:.1f}%** of total {y}."
        )

    return "\n\n".join(insight)