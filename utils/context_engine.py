import pandas as pd


def detect_dataset_context(df):

    context = {
        "domain": "General Business",
        "possible_targets": [],
        "date_columns": [],
        "currency_columns": [],
        "id_columns": [],
        "categorical_columns": [],
        "numeric_columns": []
    }

    # Detect columns
    for col in df.columns:

        col_name = str(col).lower()

        if "date" in col_name or "time" in col_name:
            context["date_columns"].append(col)

        if "id" in col_name:
            context["id_columns"].append(col)

        if any(word in col_name for word in [
            "price",
            "sales",
            "revenue",
            "profit",
            "income",
            "cost",
            "amount"
        ]):
            context["currency_columns"].append(col)

        if pd.api.types.is_numeric_dtype(df[col]):
            context["numeric_columns"].append(col)
        else:
            context["categorical_columns"].append(col)

    joined = " ".join(str(c).lower() for c in df.columns)

    if any(word in joined for word in [
        "sales",
        "customer",
        "profit",
        "revenue",
        "product"
    ]):
        context["domain"] = "Retail Sales"

    elif any(word in joined for word in [
        "employee",
        "salary",
        "department",
        "attrition"
    ]):
        context["domain"] = "Human Resources"

    elif any(word in joined for word in [
        "loan",
        "credit",
        "bank",
        "balance"
    ]):
        context["domain"] = "Finance"

    elif any(word in joined for word in [
        "patient",
        "hospital",
        "disease"
    ]):
        context["domain"] = "Healthcare"

    return context