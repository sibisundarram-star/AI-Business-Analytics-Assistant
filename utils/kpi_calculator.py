import pandas as pd


def calculate_kpi(df, question, schema):

    question = question.lower()

    if "top" in question or "bottom" in question:
        return None

    sales = schema.get("sales")
    quantity = schema.get("quantity")

    if sales is None and quantity is None:
        return None

    # -----------------------------
    # SALES KPIs
    # -----------------------------

    if sales is not None:

        if any(word in question for word in [
            "total sales",
            "total revenue",
            "sales total",
            "revenue",
            "sales in",
            "revenue in",
            "sales after",
            "revenue after",
            "sales before",
            "revenue before",
            "sales between",
            "revenue between"
        ]):

            return {
                "title": "Total Sales",
                "value": f"{df[sales].sum():,.2f}"
            }

        if any(word in question for word in [
            "average sales",
            "average revenue",
            "avg sales",
            "avg revenue"
        ]):

            return {
                "title": "Average Sales",
                "value": f"{df[sales].mean():,.2f}"
            }

        if any(word in question for word in [
            "highest sale",
            "maximum sale",
            "max sale"
        ]):

            return {
                "title": "Highest Sale",
                "value": f"{df[sales].max():,.2f}"
            }

        if any(word in question for word in [
            "lowest sale",
            "minimum sale",
            "min sale"
        ]):

            return {
                "title": "Lowest Sale",
                "value": f"{df[sales].min():,.2f}"
            }

    # -----------------------------
    # QUANTITY KPIs
    # -----------------------------

    if quantity is not None:

        if any(word in question for word in [
            "total quantity",
            "total units"
        ]):

            return {
                "title": "Total Quantity",
                "value": int(df[quantity].sum())
            }

        if any(word in question for word in [
            "average quantity",
            "avg quantity"
        ]):

            return {
                "title": "Average Quantity",
                "value": round(df[quantity].mean(), 2)
            }

    return None