def recommend_visualizations(profile):

    prompt = profile["prompt"].lower()

    visuals = []

    # Vehicle Sales
    if any(word in prompt for word in [
        "sellingprice",
        "vehicle",
        "car",
        "odometer",
        "transmission"
    ]):

        visuals = [
            ("Bar Chart", "Average Selling Price by Brand"),
            ("Scatter Plot", "Selling Price vs Odometer"),
            ("Pie Chart", "Automatic vs Manual Vehicles"),
            ("Histogram", "Selling Price Distribution"),
            ("Line Chart", "Average Price by Manufacturing Year")
        ]

    # Retail
    elif any(word in prompt for word in [
        "sales",
        "revenue",
        "customer",
        "product"
    ]):

        visuals = [
            ("Line Chart", "Monthly Revenue"),
            ("Bar Chart", "Top Products"),
            ("Pie Chart", "Sales by Category"),
            ("Map", "Regional Sales"),
            ("Scatter Plot", "Revenue vs Profit")
        ]

    # Healthcare
    elif any(word in prompt for word in [
        "patient",
        "hospital",
        "disease"
    ]):

        visuals = [
            ("Bar Chart", "Disease Distribution"),
            ("Histogram", "Patient Age"),
            ("Pie Chart", "Treatment Types"),
            ("Line Chart", "Admissions Over Time"),
            ("Scatter Plot", "Blood Pressure vs Age")
        ]

    # HR
    elif any(word in prompt for word in [
        "employee",
        "salary",
        "department"
    ]):

        visuals = [
            ("Bar Chart", "Employees by Department"),
            ("Histogram", "Salary Distribution"),
            ("Pie Chart", "Gender Distribution"),
            ("Box Plot", "Salary by Department")
        ]

    else:

        visuals = [
            ("Histogram", "Numeric Column Distribution"),
            ("Correlation Heatmap", "Numeric Relationships"),
            ("Missing Values Chart", "Data Quality")
        ]

    return visuals
