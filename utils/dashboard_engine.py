import pandas as pd

def build_dashboard_plan(df):

    plan = {
        "kpis": [],
        "charts": []
    }

    numeric = df.select_dtypes(include="number").columns.tolist()
    categorical = df.select_dtypes(include=["object", "category"]).columns.tolist()

    # -----------------------
    # KPI Detection
    # -----------------------

    if len(df) > 0:
        plan["kpis"].append(("Records", len(df)))

    if numeric:
        plan["kpis"].append(("Numeric Columns", len(numeric)))

    if categorical:
        plan["kpis"].append(("Categories", len(categorical)))

    # -----------------------
    # Chart Recommendation
    # -----------------------

    for col in numeric:
        plan["charts"].append({
            "type": "histogram",
            "column": col
        })

    for col in categorical:
        plan["charts"].append({
            "type": "bar",
            "column": col
        })

    return plan