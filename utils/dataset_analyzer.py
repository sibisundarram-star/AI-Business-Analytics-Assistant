import pandas as pd


def analyze_dataset(df):
    """Analyze a dataframe and return useful metadata."""

    info = {}

    info["rows"] = df.shape[0]
    info["columns"] = df.shape[1]

    info["column_names"] = list(df.columns)

    info["numeric_columns"] = list(
        df.select_dtypes(include="number").columns
    )

    info["categorical_columns"] = list(
        df.select_dtypes(include=["object", "category"]).columns
    )

    info["missing_values"] = (
        df.isnull()
          .sum()
          .to_dict()
    )

    info["duplicate_rows"] = int(df.duplicated().sum())

    info["data_types"] = (
        df.dtypes
          .astype(str)
          .to_dict()
    )

    return info