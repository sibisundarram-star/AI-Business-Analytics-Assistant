import pandas as pd


SUPPORTED_OPERATIONS = {
    "count",
    "sum",
    "average",
    "minimum",
    "maximum",
    "group_by",
    "top_n",
    "filter",
    "describe",
}


def validate_plan(plan, df):
    """
    Validate an analytical plan before executing it.
    """

    if not isinstance(plan, dict):
        raise ValueError("Analysis plan must be a dictionary.")

    if not plan.get("understood", False):
        raise ValueError("The question could not be understood.")

    operation = plan.get("operation")

    if operation not in SUPPORTED_OPERATIONS:
        raise ValueError(f"Unsupported operation: {operation}")

    # Validate referenced columns
    columns_to_check = [
        plan.get("column"),
        plan.get("group_by"),
    ]

    for column in columns_to_check:
        if column is not None and column not in df.columns:
            raise ValueError(
                f"Column '{column}' does not exist in the dataset."
            )

    # Validate filters
    for filter_rule in plan.get("filters", []):
        column = filter_rule.get("column")

        if column not in df.columns:
            raise ValueError(
                f"Filter column '{column}' does not exist."
            )

    return True


def apply_filters(df, filters):
    """
    Apply supported filters to a dataframe.
    """

    result = df.copy()

    for rule in filters or []:

        column = rule.get("column")
        operator = rule.get("operator")
        value = rule.get("value")

        if operator == "equals":
            result = result[
                result[column].astype(str).str.lower()
                == str(value).lower()
            ]

        elif operator == "contains":
            result = result[
                result[column]
                .astype(str)
                .str.contains(
                    str(value),
                    case=False,
                    na=False
                )
            ]

        else:
            raise ValueError(
                f"Unsupported filter operator: {operator}"
            )

    return result


def execute_plan(plan, df):
    """
    Execute an LLM-generated analytical plan using Pandas.

    The LLM decides what should be calculated.
    Pandas performs the actual calculation.
    """

    validate_plan(plan, df)

    operation = plan["operation"]
    column = plan.get("column")
    group_by = plan.get("group_by")
    filters = plan.get("filters", [])

    working_df = apply_filters(df, filters)

    # --------------------------------------------------
    # FILTER
    # --------------------------------------------------

    if operation == "filter":

        return {
            "message": (
                f"Found {len(working_df):,} matching rows."
            ),
            "table": working_df,
            "chart": None,
        }

    # --------------------------------------------------
    # COUNT
    # --------------------------------------------------

    if operation == "count":

        count = len(working_df)

        return {
            "message": f"Count: {count:,}",
            "table": None,
            "chart": None,
        }

    # --------------------------------------------------
    # GROUP BY
    # --------------------------------------------------

    if operation == "group_by":

        if group_by is None:
            raise ValueError(
                "A group_by column is required."
            )

        grouped = (
            working_df
            .groupby(group_by)
            .size()
            .reset_index(name="Count")
            .sort_values("Count", ascending=False)
        )

        return {
            "message": (
                f"Grouped {len(working_df):,} rows by "
                f"'{group_by}'."
            ),
            "table": grouped,
            "chart": {
                "type": "bar",
                "data": grouped,
                "x": group_by,
                "y": "Count",
            },
        }

    # --------------------------------------------------
    # SUM
    # --------------------------------------------------

    if operation == "sum":

        if column is None:
            raise ValueError(
                "A numeric column is required for sum."
            )

        if not pd.api.types.is_numeric_dtype(
            working_df[column]
        ):
            raise ValueError(
                f"'{column}' is not numeric."
            )

        total = working_df[column].sum()

        return {
            "message": (
                f"Total {column}: {total:,.2f}"
            ),
            "table": None,
            "chart": None,
        }

    # --------------------------------------------------
    # AVERAGE
    # --------------------------------------------------

    if operation == "average":

        if column is None:
            raise ValueError(
                "A numeric column is required for average."
            )

        if not pd.api.types.is_numeric_dtype(
            working_df[column]
        ):
            raise ValueError(
                f"'{column}' is not numeric."
            )

        average = working_df[column].mean()

        return {
            "message": (
                f"Average {column}: {average:,.2f}"
            ),
            "table": None,
            "chart": None,
        }

    # --------------------------------------------------
    # MINIMUM
    # --------------------------------------------------

    if operation == "minimum":

        if column is None:
            raise ValueError(
                "A numeric column is required."
            )

        value = working_df[column].min()

        return {
            "message": (
                f"Minimum {column}: {value}"
            ),
            "table": None,
            "chart": None,
        }

    # --------------------------------------------------
    # MAXIMUM
    # --------------------------------------------------

    if operation == "maximum":

        if column is None:
            raise ValueError(
                "A numeric column is required."
            )

        value = working_df[column].max()

        return {
            "message": (
                f"Maximum {column}: {value}"
            ),
            "table": None,
            "chart": None,
        }

    # --------------------------------------------------
    # TOP N
    # --------------------------------------------------

    if operation == "top_n":

        if column is None:
            raise ValueError(
                "A column is required for top_n."
            )

        if not pd.api.types.is_numeric_dtype(
            working_df[column]
        ):
            raise ValueError(
                f"'{column}' must be numeric for top_n."
            )

        n = plan.get("n") or 10

        result = (
            working_df
            .nlargest(n, column)
            .reset_index(drop=True)
        )

        return {
            "message": (
                f"Top {n} rows by '{column}'."
            ),
            "table": result,
            "chart": None,
        }

    # --------------------------------------------------
    # DESCRIBE
    # --------------------------------------------------

    if operation == "describe":

        result = working_df.describe(
            include="all"
        ).transpose().reset_index()

        return {
            "message": "Dataset statistical summary.",
            "table": result,
            "chart": None,
        }

    raise ValueError(
        f"Operation '{operation}' is not implemented."
    )