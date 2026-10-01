def apply_filters(df, filters, schema):

    if "country" in filters:

        col = schema["country"]

        df = df[
            df[col]
            .astype(str)
            .str.lower()
            ==
            filters["country"].lower()
        ]

    if "product" in filters:

        col = schema.get("product")

        df = df[
            df[col]
            .astype(str)
            .str.lower()
            ==
            filters["product"].lower()
        ]

    if "customer" in filters:

        col = schema["customer"]

        df = df[
            df[col]
            .astype(str)
            .str.lower()
            ==
            filters["customer"].lower()
        ]

    return df