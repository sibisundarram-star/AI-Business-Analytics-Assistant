import pandas as pd


def get_dataset_overview(df):
    """
    Returns basic information about the dataset.
    """

    overview = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing": int(df.isnull().sum().sum()),
        "duplicates": int(df.duplicated().sum()),
        "memory": round(df.memory_usage(deep=True).sum() / (1024 ** 2), 2)
    }

    return overview