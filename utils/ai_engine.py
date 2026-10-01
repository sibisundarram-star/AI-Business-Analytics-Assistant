import pandas as pd



def find_column(question, df):
    """
    Finds a dataframe column mentioned in the user's question.
    """

    question = question.lower()

    categorical = df.select_dtypes(include=["object", "category"]).columns

    for column in df.columns:
        if column.lower() in question:
            return column

    return None

def find_categorical_column(question, df):
    """
    Finds a categorical column mentioned in the user's question.
    """

    question = question.lower()

    categorical = df.select_dtypes(include=["object", "category"]).columns

    for column in categorical:
        if column.lower() in question:
            return column

    return None

def filter_dataframe(question, df):
    """
    Filters a dataframe using categorical values found in the question.
    """

    question = question.lower()

    for column in df.select_dtypes(include=["object", "category"]).columns:

        for value in df[column].dropna().unique():

            if str(value).lower() in question:

                filtered = df[df[column] == value]

                return (
                    f"Found {len(filtered)} matching rows.",
                    filtered
                )

    return None, None

def sort_dataframe(question, df):
    """
    Returns top or bottom rows of a numeric column.
    """

    question = question.lower()

    column = find_column(question, df)

    if column is None:
        return None, None

    if not pd.api.types.is_numeric_dtype(df[column]):
        return None, None

    # Default number of rows
    n = 10

    words = question.split()

    for word in words:
        if word.isdigit():
            n = int(word)
            break

    if "top" in question or "highest" in question:

        result = df.nlargest(n, column)

        return (
            f"Top {n} rows by {column}",
            result
        )

    if "bottom" in question or "lowest" in question:

        result = df.nsmallest(n, column)

        return (
            f"Bottom {n} rows by {column}",
            result
        )

    return None, None


def ask_ai(question, df):

    question = question.lower()
    message, filtered_df = filter_dataframe(question, df)

    if filtered_df is not None:

        return {
            "message": message,
            "table": filtered_df,
            "chart": None
        }
    message, sorted_df = sort_dataframe(question, df)

    if sorted_df is not None:

        return {
            "message": message,
            "table": sorted_df,
            "chart": None
        }

    # Duplicate rows
    if "duplicate" in question:
        return {
            "message": f"The dataset contains {df.duplicated().sum():,} duplicate rows.",
            "table": None,
            "chart": None
        }

    # Missing values
    if "missing" in question:
        return {
            "message": f"The dataset contains {df.isnull().sum().sum():,} missing values.",
            "table": None,
            "chart": None
        }

    # Numeric columns
    if "numeric" in question:
        cols = df.select_dtypes(include="number").columns.tolist()
        return {
            "message": "Numeric columns:\n\n" + "\n".join(f"• {c}" for c in cols),
            "table": None,
            "chart": None
        }

    # Categorical columns
    if "categorical" in question or "text" in question:
        cols = df.select_dtypes(include="object").columns.tolist()
        return {
            "message": "Categorical columns:\n\n" + "\n".join(f"• {c}" for c in cols),
            "table": None,
            "chart": None
        }

    # Memory
    if "memory" in question:
        memory = round(df.memory_usage(deep=True).sum() / (1024 ** 2), 2)
        return {
            "message": f"Dataset memory usage: {memory} MB",
            "table": None,
            "chart": None
        }

    # List columns
    if "columns" in question:
        return {
            "message": "\n".join(df.columns),
            "table": None,
            "chart": None
        }

    # Row count
    if "row" in question:
        return {
            "message": f"The dataset contains {len(df):,} rows.",
            "table": None,
            "chart": None
        }

    # Column count
    if "column" in question:
        return {
            "message": f"The dataset contains {len(df.columns)} columns.",
            "table": None,
            "chart": None
        }

    ##################################################
    # NEW ANALYTICS
    ##################################################

    column = find_column(question, df)
    group_column = find_categorical_column(question, df)
    print(column)
    print(group_column)
    
    ##################################################
    # GROUP BY ANALYSIS
    ##################################################

    if column and group_column:

        if column == group_column:
            return "Please specify a numeric column and a grouping column."

        if not pd.api.types.is_numeric_dtype(df[column]):
            return f"'{column}' is not numeric."

        if "average" in question or "mean" in question:

            result = (
                df.groupby(group_column)[column]
                .mean()
                .sort_values(ascending=False)
                .reset_index()
            )

            return {
                "message": result.to_string(index=False),
                "chart": {
                    "type": "bar",
                    "data": result,
                    "x": group_column,
                    "y": column
                }
            }

        if "total" in question or "sum" in question:

            result = (
                df.groupby(group_column)[column]
                .sum()
                .sort_values(ascending=False)
                .reset_index()
            )

            return {
                "message": result.to_string(index=False),
                "chart": {
                    "type": "bar",
                    "data": result,
                    "x": group_column,
                    "y": column
                }
        }

        

        if "count" in question:

            result = (
                df.groupby(group_column)
                .size()
                .sort_values(ascending=False)
            )

            return {
                "message": result.to_string(),
                "chart": {
                    "type": "bar",
                    "data": result.reset_index(),
                    "x": group_column,
                    "y": column
                }
            }
       

    ##################################################
    # SINGLE COLUMN ANALYSIS
    ##################################################

    if column is not None:  

        if not pd.api.types.is_numeric_dtype(df[column]):
            return f"'{column}' is not a numeric column."

        if "average" in question or "mean" in question:
            return {
                "message": f"Average {column}: {df[column].mean():.2f}",
                "chart": None,
                "table": None
            }

        if "sum" in question or "total" in question:
            return {
                "message": f"Total {column}: {df[column].sum():,.2f}",
                "chart": None,
                "table": None
            }

        if "maximum" in question or "highest" in question or "max" in question:
            return {
                "message": f"Maximum {column}: {df[column].max():,.2f}",
                "chart": None,
                "table": None
            }

        if "minimum" in question or "lowest" in question or "min" in question:
            return {
                "message": f"Minimum {column}: {df[column].min():,.2f}",
                "chart": None,
                "table": None
            }

    return {
        "message": "Sorry, I couldn't understand that request.",
        "table": None,
        "chart": None
    }