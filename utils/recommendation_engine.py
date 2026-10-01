def generate_recommendation(chart_df, x, y):

    if chart_df.empty:
        return "No recommendation available."

    highest = chart_df.loc[chart_df[y].idxmax()]
    lowest = chart_df.loc[chart_df[y].idxmin()]

    recommendations = []

    recommendations.append(
        f"Consider investing more resources in **{highest[x]}**, as it currently delivers the strongest performance."
    )

    recommendations.append(
        f"Review business strategy for **{lowest[x]}** to identify reasons for lower performance."
    )

    if len(chart_df) >= 5:

        top5_share = (
            chart_df.nlargest(5, y)[y].sum()
            / chart_df[y].sum()
        ) * 100

        if top5_share > 70:

            recommendations.append(
                "Revenue is highly concentrated. Expanding into lower-performing categories or regions may reduce dependency."
            )

    return recommendations