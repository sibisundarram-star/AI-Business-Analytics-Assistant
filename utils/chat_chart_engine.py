from duckdb import query
import pandas as pd
from utils.ranking_engine import detect_ranking
from utils.schema_interpreter import interpret_schema
from utils.query_parser import parse_query
from utils.column_finder import find_best_column


def chart_request(question, df):

    question = question.lower()
   

    schema = interpret_schema(df)
    query = parse_query(question, df)

    numeric_columns = [
        c for c in df.columns
        if pd.api.types.is_numeric_dtype(df[c])
    ]

    categorical_columns = [
        c for c in df.columns
        if not pd.api.types.is_numeric_dtype(df[c])
    ]

    chart_type = query["chart"]
    
    top_n = query["top_n"]
    
    bottom_n = query["bottom_n"]

    x = query["dimension"]
    y = query["metric"]

    print("X =", x)
    print("Y =", y)
    print("Aggregation =", query["aggregation"])

    # -------------------------
    # Dynamic Column Detection
    # -------------------------

    if x is None:
        x = find_best_column(question, schema)

    if y is None:
        if schema["metrics"]:
            y = schema["metrics"][0]

    # -------------------------
    # Metric fallback
    # -------------------------

    if y is None:

        if any(word in question for word in [
            "sales", "sale", "revenue", "income", "turnover"
        ]):
            y = schema.get("sales")

        elif any(word in question for word in [
            "quantity", "qty", "units"
        ]):
            y = schema.get("quantity")

    # -------------------------
    # Final safety fallback
    # -------------------------

    if x is None and categorical_columns:
        x = categorical_columns[0]

    if y is None and numeric_columns:
        y = numeric_columns[0]

    print("Detected X:", x)
    print("Detected Y:", y)
    print("---------------")
    print("Question:", question)
    print("Chart:", chart_type)
    print("X:", x)
    print("Y:", y)
    print("Top:", top_n)
    print("Bottom:", bottom_n)
    print("---------------")

    return True, chart_type, x, y, top_n, bottom_n