import pandas as pd
from utils.schema_interpreter import interpret_schema


def generate_dataset_summary(df):

    schema = interpret_schema(df)

    sales_col = schema.get("sales")
    customer_col = schema.get("customer")
    country_col = schema.get("country")
    product_col = schema.get("product")

    total_sales = (
        df[sales_col].sum()
        if sales_col else 0
    )

    total_customers = (
        df[customer_col].nunique()
        if customer_col else 0
    )

    total_countries = (
        df[country_col].nunique()
        if country_col else 0
    )

    total_products = (
        df[product_col].nunique()
        if product_col else 0
    )

    top_country = None

    if country_col and sales_col:

        top_country = (
            df.groupby(country_col)[sales_col]
            .sum()
            .idxmax()
        )

    summary = f"""
### 📊 Executive Summary

💰 Total Sales: **${total_sales:,.2f}**

👥 Customers: **{total_customers:,}**

🌍 Countries: **{total_countries:,}**

📦 Products: **{total_products:,}**

🏆 Highest Revenue Country: **{top_country}**
"""

    return summary