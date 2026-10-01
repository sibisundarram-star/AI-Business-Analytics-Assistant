import pandas as pd
from utils.schema_interpreter import interpret_schema


def generate_trend(df, question):

    schema = interpret_schema(df)

    date_col = schema.get("date")
    sales_col = schema.get("sales")

    if date_col is None or sales_col is None:
        return None

    df = df.copy()

    df[date_col] = pd.to_datetime(df[date_col])

    question = question.lower()

    # Monthly trend (default)
    if (
        "trend" in question
        or "over time" in question
        or "monthly" in question
        or "month" in question
    ):

        trend = (
            df.groupby(df[date_col].dt.to_period("M"))[sales_col]
            .sum()
            .reset_index()
        )

        trend[date_col] = trend[date_col].astype(str)

        return trend, date_col, sales_col, "Line Chart"
    

    # Quarterly trend
    if "quarter" in question:

        trend = (
            df.groupby(df[date_col].dt.to_period("Q"))[sales_col]
            .sum()
            .reset_index()
        )

        trend[date_col] = trend[date_col].astype(str)

        return trend, date_col, sales_col, "Line Chart"

    # Yearly trend
    if "year" in question or "yearly" in question:

        trend = (
            df.groupby(df[date_col].dt.year)[sales_col]
            .sum()
            .reset_index()
        )

        return trend, date_col, sales_col, "Line Chart"

    return None