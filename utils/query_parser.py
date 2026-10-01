import re
from duckdb import df
import pandas as pd


def parse_query(question, df):

    question = question.lower()

    query = {
        "chart": "Bar Chart",
        "metric": None,
        "dimension": None,
        "aggregation": "sum",
        "top_n": None,
        "bottom_n": None,
        "filters": {}
    }

    # -------------------------
    # Chart Type
    # -------------------------

    if "line" in question:
        query["chart"] = "Line Chart"

    elif "scatter" in question:
        query["chart"] = "Scatter Plot"

    elif "pie" in question:
        query["chart"] = "Pie Chart"

    elif "histogram" in question:
        query["chart"] = "Histogram"

    elif "box" in question:
        query["chart"] = "Box Plot"

    # -------------------------
    # Aggregation
    # -------------------------

    if any(w in question for w in ["average", "avg", "mean"]):
        query["aggregation"] = "mean"

    elif any(w in question for w in ["maximum", "max", "highest"]):
        query["aggregation"] = "max"

    elif any(w in question for w in ["minimum", "min", "lowest"]):
        query["aggregation"] = "min"

    elif (
        "count" in question
        or "number of" in question
        or "how many" in question
    ):
        query["aggregation"] = "count"

    # -------------------------
    # Top / Bottom
    # -------------------------

    top = re.search(r"top\s+(\d+)", question)
    bottom = re.search(r"bottom\s+(\d+)", question)

    if top:
        query["top_n"] = int(top.group(1))

    if bottom:
        query["bottom_n"] = int(bottom.group(1))

    # -------------------------
    # Detect columns
    # -------------------------

    for col in df.columns:

        clean = col.lower().replace("_", " ")

        # Dimension keywords
        if any(word in question for word in [clean, clean.rstrip("s")]):

           if pd.api.types.is_numeric_dtype(df[col]):
               query["metric"] = col
           else:
               query["dimension"] = col


    # -------------------------
    # Intelligent fallbacks
    # -------------------------

    if query["dimension"] is None:

        for col in df.columns:

            name = col.lower()

            if any(k in question for k in ["country", "countries", "nation", "region", "state"]):
                if "country" in name or "region" in name or "state" in name:
                    query["dimension"] = col
                    break

            elif any(k in question for k in ["product", "products", "item", "category"]):
                if any(w in name for w in ["product", "item", "category"]):
                    query["dimension"] = col
                    break

            elif any(k in question for k in ["customer", "client", "buyer"]):
                if any(w in name for w in ["customer", "client", "buyer"]):
                    query["dimension"] = col
                    break

            elif any(k in question for k in ["month", "monthly", "date", "trend", "year"]):
                if any(w in name for w in ["date", "month", "year"]):
                    query["dimension"] = col
                    break
    print(query)
    return query