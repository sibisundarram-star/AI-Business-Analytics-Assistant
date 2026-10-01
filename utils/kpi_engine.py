def recommend_kpis(profile):

    prompt = profile["prompt"].lower()

    kpis = []

    # Retail
    if any(word in prompt for word in [
        "sales", "revenue", "customer", "product", "profit"
    ]):
        kpis = [
            "Total Revenue",
            "Average Order Value",
            "Profit Margin",
            "Customer Count",
            "Monthly Sales Growth",
            "Top Products"
        ]

    # Vehicle
    elif any(word in prompt for word in [
        "sellingprice",
        "vehicle",
        "car",
        "odometer",
        "transmission",
        "vin"
    ]):
        kpis = [
            "Average Selling Price",
            "Median Selling Price",
            "Average Odometer",
            "Vehicle Count",
            "Average Vehicle Age",
            "Top Selling Brands"
        ]

    # Healthcare
    elif any(word in prompt for word in [
        "patient",
        "hospital",
        "disease",
        "diagnosis",
        "treatment"
    ]):
        kpis = [
            "Total Patients",
            "Average Patient Age",
            "Disease Distribution",
            "Treatment Success Rate",
            "Average Blood Pressure"
        ]

    # HR
    elif any(word in prompt for word in [
        "employee",
        "salary",
        "department",
        "attrition"
    ]):
        kpis = [
            "Employee Count",
            "Average Salary",
            "Attrition Rate",
            "Department Distribution"
        ]

    else:
        kpis = [
            "Record Count",
            "Missing Value %",
            "Duplicate Records",
            "Top Categories"
        ]

    return kpis