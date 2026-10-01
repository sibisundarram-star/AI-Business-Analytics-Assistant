import pandas as pd


def generate_insights(df):
    """
    Generate basic business insights from a dataset.
    """

    insights = []

    # Dataset size
    insights.append(
        f"Dataset contains {len(df):,} rows and {len(df.columns)} columns."
    )

    # Missing values
    missing = df.isnull().sum().sum()

    if missing == 0:
        insights.append("No missing values detected.")
    else:
        insights.append(f"Dataset contains {missing:,} missing values.")

    # Duplicate rows
    duplicates = df.duplicated().sum()

    if duplicates == 0:
        insights.append("No duplicate rows found.")
    else:
        insights.append(f"Dataset contains {duplicates:,} duplicate rows.")

    # Numeric & categorical columns
    numeric = len(df.select_dtypes(include="number").columns)
    categorical = len(df.select_dtypes(include="object").columns)

    insights.append(
        f"The dataset has {numeric} numeric columns and {categorical} categorical columns."
    )

    return insights