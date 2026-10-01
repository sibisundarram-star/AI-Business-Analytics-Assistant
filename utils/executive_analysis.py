from utils.schema_interpreter import interpret_schema


def generate_executive_analysis(df):

    schema = interpret_schema(df)

    sales = schema.get("sales")
    country = schema.get("country")
    product = schema.get("product")

    # Dataset not compatible with sales analysis
    if not sales or not country or not product:
        return (
            f"Dataset contains **{len(df):,}** records.\n\n"
            f"Primary Metric: **{schema.get('primary_metric', 'Unknown')}**.\n\n"
            "Detailed executive analysis is unavailable for this dataset."
        )

    analysis = []

    analysis.append(
        f"• Total revenue is ${df[sales].sum():,.0f}."
    )

    top_country = (
        df.groupby(country)[sales]
        .sum()
        .idxmax()
    )

    analysis.append(
        f"• {top_country} is the highest revenue contributor."
    )

    top_product = (
        df.groupby(product)[sales]
        .sum()
        .idxmax()
    )

    analysis.append(
        f"• {top_product} contributes the highest product revenue."
    )

    return "\n".join(analysis)