import re


def apply_date_filter(df, question, schema):

    date_col = schema.get("date")

    if date_col is None:
        return df

    question = question.lower()

    if not hasattr(df[date_col], "dt"):
        return df

    years = re.findall(r"\b(19\d{2}|20\d{2})\b", question)

    # Sales in 2004
    if len(years) == 1 and "after" not in question and "before" not in question:

        year = int(years[0])

        return df[
            df[date_col].dt.year == year
        ]

    # Sales after 2004
    if "after" in question and len(years) == 1:

        year = int(years[0])

        return df[
            df[date_col].dt.year > year
        ]

    # Sales before 2004
    if "before" in question and len(years) == 1:

        year = int(years[0])

        return df[
            df[date_col].dt.year < year
        ]

    # Between 2003 and 2005
    if "between" in question and len(years) == 2:

        start = int(years[0])
        end = int(years[1])

        return df[
            (df[date_col].dt.year >= start)
            &
            (df[date_col].dt.year <= end)
        ]

    return df