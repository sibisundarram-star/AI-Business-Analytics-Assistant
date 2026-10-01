import pandas as pd


def statistics_handler(question, df, dataset_info):

    question = question.lower()

    if any(word in question for word in [
        "row",
        "record",
        "entry",
        "observation",
        "size"
    ]):

        return (
            f"Your dataset contains **{dataset_info['rows']:,} rows** "
            f"and **{dataset_info['columns']} columns**."
        )

    if "column" in question:
        return (
            f"The dataset contains **{dataset_info['columns']} columns**."
        )

    if "missing" in question:

        total = df.isnull().sum().sum()

        return f"There are **{total:,} missing values**."

    if "duplicate" in question:

        return (
            f"I found **{dataset_info['duplicate_rows']} duplicate rows**."
        )

    return "Could you be more specific about the statistic you need?"