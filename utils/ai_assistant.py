from warnings import filters

from duckdb import df
import pandas as pd
from utils.conversation_memory import merge_query
from utils.filter_executor import apply_filters
from utils.intent_engine import detect_intent
from utils.handlers.statistics import statistics_handler
from utils.chat_chart_engine import chart_request
from utils.kpi_calculator import calculate_kpi
from utils.date_filter import apply_date_filter
from utils.query_filter_parser import extract_filters
from utils.schema_interpreter import interpret_schema
from utils.comparison_handler import compare_entities
from utils.filter_engine import apply_business_filters
from utils.comparison_engine import detect_comparison
from utils.trend_engine import generate_trend

def answer_question(question, df, dataset_info, last_query=None):

    question = merge_query(question, last_query)
    original_question = question
    question = question.lower()
    intent = detect_intent(question)
    schema = interpret_schema(df)
    df = apply_date_filter(
        df,
        question,
        schema
    )
    
    trend = generate_trend(df, question)

    if trend is not None:

        trend_df, x, y, chart = trend

        return {
            "type": "trend",
            "data": trend_df,
            "chart": chart,
            "x": x,
            "y": y
        }
    print(df["ORDERDATE"].min())
    print(df["ORDERDATE"].max())
    print("Rows after date filter:", len(df))
    if "top" in question or "bottom"  in question:
        kpi = calculate_kpi(df, question, schema)

        print("KPI:", kpi)
        print("Question:", question)

        if kpi is not None:
            return {
                    "type": "kpi",
                    "title": kpi["title"],
                    "value": kpi["value"]
                }
    
    comparison = detect_comparison(question)

    if comparison is not None:

        entity1, entity2 = comparison

        comparison_df = compare_entities(
            df,
            schema,
            entity1,
            entity2
        )   

        return {
            "type": "comparison",
            "data": comparison_df,
            "x": schema["country"],
            "y": schema["sales"]
        }
    filters = extract_filters(df, question)

    df = apply_filters(
        df,
        filters,
        schema
    )
    
    is_chart, chart_type, x, y, top_n, bottom_n = chart_request(
        question,
        df
    )
    
    if is_chart:
        return {
            "type": "chart",
            "chart": chart_type,
            "x": x,
            "y": y,
            "top_n": top_n,
            "bottom_n": bottom_n,
            "data": df
        }

    # Greeting
    if any(word in question for word in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]):
        return (
            "Hello! 👋 I'm your AI Business Analytics Assistant. "
            "Ask me anything about your dataset."
        )
    

    # -----------------------------
    # Statistics Intent
    # -----------------------------

    if intent == "statistics":
        return statistics_handler(
             question,
                df,
                dataset_info
            )

    # -----------------------------
    # Highest / Lowest
    # -----------------------------
    if "highest" in question or "maximum" in question:

        numeric = df.select_dtypes(include="number")

        if numeric.empty:
            return "There are no numerical columns."

        col = numeric.mean().idxmax()

        return f"The numeric column with the highest average value is **{col}**."

    if "lowest" in question or "minimum" in question:

        numeric = df.select_dtypes(include="number")

        if numeric.empty:
            return "There are no numerical columns."

        col = numeric.mean().idxmin()

        return f"The numeric column with the lowest average value is **{col}**."

    # -----------------------------
    # Average
    # -----------------------------
    if "average" in question or "mean" in question:

        for column in df.columns:

            if column.lower() in question:

                if pd.api.types.is_numeric_dtype(df[column]):

                    avg = df[column].mean()

                    return f"The average of **{column}** is **{avg:,.2f}**."

        return "Please mention the column name."

    # -----------------------------
    # Most Common
    # -----------------------------
    if "most common" in question or "most frequent" in question:

        for column in df.columns:

            if column.lower() in question:

                value = df[column].mode()[0]

                return f"The most common value in **{column}** is **{value}**."

    # -----------------------------
    # Unique Values
    # -----------------------------
    if "unique" in question:

        for column in df.columns:

            if column.lower() in question:

                count = df[column].nunique()

                return f"**{column}** contains **{count} unique values**."

    # -----------------------------
    # Correlation
    # -----------------------------
    if "correlation" in question:

        return "Correlation analysis will be available in Version 4."

    # -----------------------------
    # Machine Learning
    # -----------------------------
    if "machine learning" in question:

        return (
            "This dataset appears suitable for machine learning if "
            "it contains a target column and sufficient cleaned data."
        )

    # -----------------------------
    # Insights
    # -----------------------------
    if intent == "summary":

        return f"""
### Here are my observations:

• Dataset has **{dataset_info['rows']:,} records**

• There are **{dataset_info['columns']} columns**

• Duplicate rows: **{dataset_info['duplicate_rows']}**

• Missing values: **{df.isnull().sum().sum():,}**

• Numeric columns: **{len(dataset_info['numeric_columns'])}**

• Categorical columns: **{len(dataset_info['categorical_columns'])}**
"""

    return (
        "I'm not able to answer that yet, but I'm learning. "
        "Try asking about rows, averages, missing values, unique values, "
        "insights, duplicates, or machine learning suitability."
    )