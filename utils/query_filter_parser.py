from utils.schema_interpreter import interpret_schema


def extract_filters(df, question):

    schema = interpret_schema(df)

    filters = {}

    question = question.lower()

    # COUNTRY
    if schema.get("country"):

        col = schema["country"]

        for value in df[col].dropna().unique():

            if str(value).lower() in question:

                filters["country"] = value

                break

    # PRODUCT
    if schema.get("product"):

        col = schema.get("product")

        for value in df[col].dropna().unique():

            if str(value).lower() in question:

                filters["product"] = value

                break

    # CUSTOMER

    if schema.get("customer"):

        col = schema["customer"]

        for value in df[col].dropna().unique():

            if str(value).lower() in question:

                filters["customer"] = value

                break

    return filters