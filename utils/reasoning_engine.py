def generate_business_reasoning(profile):

    prompt = profile["prompt"].lower()

    reasoning = []

    # -------------------------
    # Retail / Sales
    # -------------------------

    if any(word in prompt for word in [
        "sales",
        "revenue",
        "customer",
        "product",
        "profit"
    ]):

        reasoning.append(
            "The dataset appears to support business performance analysis."
        )

        reasoning.append(
            "Management can use this data to identify revenue drivers and improve profitability."
        )

    # -------------------------
    # Vehicle
    # -------------------------

    if any(word in prompt for word in [
        "sellingprice",
        "odometer",
        "vin",
        "transmission",
        "vehicle",
        "car"
    ]):

        reasoning.append(
            "This dataset appears to represent historical vehicle sales."
        )

        reasoning.append(
            "The primary objective is likely resale price prediction and inventory optimisation."
        )

    # -------------------------
    # Healthcare
    # -------------------------

    if any(word in prompt for word in [
        "patient",
        "hospital",
        "disease"
    ]):

        reasoning.append(
            "The dataset appears to support clinical decision making and patient outcome analysis."
        )

    # -------------------------
    # HR
    # -------------------------

    if any(word in prompt for word in [
        "employee",
        "salary",
        "department",
        "attrition"
    ]):

        reasoning.append(
            "The dataset appears to support workforce analytics."
        )

    return reasoning