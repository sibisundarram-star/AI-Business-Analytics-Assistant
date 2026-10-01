def suggest_questions(question):

    question = question.lower()

    if "country" in question:
        return [
            "Compare France and Germany",
            "Top 10 countries by sales",
            "Monthly sales trend",
            "Average sales by country"
        ]

    if "customer" in question:
        return [
            "Top 10 customers",
            "Sales by customer country",
            "Average customer sales"
        ]

    if "product" in question:
        return [
            "Top 10 products",
            "Sales by product line",
            "Compare Classic Cars and Motorcycles"
        ]

    return [
        "Top 10 countries by sales",
        "Monthly sales trend",
        "Compare France and Germany",
        "Average sales by product line"
    ]