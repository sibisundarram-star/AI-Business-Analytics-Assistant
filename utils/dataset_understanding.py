import pandas as pd


def understand_dataset(df):

    info = {
        "numeric": [],
        "categorical": [],
        "dates": [],
        "identifiers": [],
        "text": [],
        "metrics": [],
        "dimensions": []
    }

    for col in df.columns:

        series = df[col]

        # Numeric
        if pd.api.types.is_numeric_dtype(series):

            info["numeric"].append(col)

            if series.nunique() > 5:
                info["metrics"].append(col)

            continue

        # Try datetime
        try:

            converted = pd.to_datetime(series)

            if converted.notna().sum() > len(series) * 0.8:

                info["dates"].append(col)
                info["dimensions"].append(col)
                continue

        except Exception:
            pass

        unique_ratio = series.nunique() / max(len(series), 1)

        # IDs
        if unique_ratio > 0.95:

            info["identifiers"].append(col)

        # Categories
        elif series.nunique() <= 50:

            info["categorical"].append(col)
            info["dimensions"].append(col)

        # Text
        else:

            info["text"].append(col)

    # -------------------------
    # Choose Primary Metric
    # -------------------------

    if info["metrics"]:
        best_metric = max(
            info["metrics"],
            key=lambda c: df[c].fillna(0).sum()
        )
        info["primary_metric"] = best_metric
    else:
        info["primary_metric"] = None

    return info