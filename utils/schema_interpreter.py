from utils.dataset_understanding import understand_dataset


def interpret_schema(df):

    info = understand_dataset(df)

    schema = {}

    # Primary metric
    if info["metrics"]:
        schema["primary_metric"] = info["primary_metric"] 

    # Available metrics
    schema["metrics"] = info["metrics"]

    # Available dimensions
    schema["dimensions"] = info["dimensions"]

    # Date column
    if info["dates"]:
        schema["date"] = info["dates"][0]

    # Best categorical dimension
    if info["categorical"]:
        schema["category"] = info["categorical"][0]

    # Keep backward compatibility
    synonyms = {
        "sales": [
            "sales",
            "revenue",
            "amount",
            "income",
            "turnover",
            "price"
        ],
        "country": [
            "country",
            "nation",
            "region",
            "state"
        ],
        "product": [
            "product",
            "item",
            "category"
        ],
        "customer": [
            "customer",
            "client",
            "buyer"
        ],
        "quantity": [
            "quantity",
            "qty",
            "units"
        ]
    }

    cols = {c.lower(): c for c in df.columns}

    for key, words in synonyms.items():

        for word in words:

            if word in cols:

                schema[key] = cols[word]
                break

    return schema