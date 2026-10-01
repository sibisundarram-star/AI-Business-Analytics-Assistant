import pandas as pd


def build_business_profile(df):

    profile = {}

    profile["rows"] = len(df)
    profile["columns"] = len(df.columns)

    profile["column_names"] = list(df.columns)

    profile["numeric"] = list(
        df.select_dtypes(include="number").columns
    )

    profile["categorical"] = list(
        df.select_dtypes(include=["object", "category"]).columns
    )

    profile["missing"] = int(df.isnull().sum().sum())

    profile["duplicates"] = int(df.duplicated().sum())

    profile["memory_mb"] = round(
        df.memory_usage(deep=True).sum() / 1024**2,
        2
    )

    profile["target_candidates"] = []

    for col in df.columns:

        name = str(col).lower()

        if any(word in name for word in [
            "price",
            "sales",
            "profit",
            "revenue",
            "income",
            "target",
            "label",
            "class",
            "salary",
            "cost",
            "amount",
            "rating",
            "score"
        ]):
            profile["target_candidates"].append(col)

    return profile