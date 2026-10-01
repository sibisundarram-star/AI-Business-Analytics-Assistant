import io
import pandas as pd


def export_csv(df):
    return df.to_csv(index=False).encode("utf-8")


def export_excel(df):
    output = io.BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Dataset")

    return output.getvalue()