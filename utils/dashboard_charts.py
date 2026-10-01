import plotly.express as px
from utils.schema_interpreter import interpret_schema


def sales_by_country(df):

    schema = interpret_schema(df)

    country = schema.get("country")
    sales = schema.get("sales")

    if country is None or sales is None:
        return None

    chart = (
        df.groupby(country)[sales]
        .sum()
        .reset_index()
        .sort_values(sales, ascending=False)
        .head(10)
    )

    fig = px.bar(
        chart,
        x=country,
        y=sales,
        title="Top 10 Countries by Sales"
    )

    return fig

def monthly_sales(df):

    schema = interpret_schema(df)

    date = schema["date"]
    sales = schema["sales"]

    chart = (
        df.groupby(df[date].dt.to_period("M"))[sales]
        .sum()
        .reset_index()
    )

    chart[date] = chart[date].astype(str)

    fig = px.line(
        chart,
        x=date,
        y=sales,
        title="Monthly Sales Trend"
    )

    return fig

def product_sales(df):

    schema = interpret_schema(df)

    product = schema.get("product")
    sales = schema.get("sales")

    if product is None or sales is None:
        return None

    chart = (
        df.groupby(product)[sales]
        .sum()
        .reset_index()
    )

    return chart