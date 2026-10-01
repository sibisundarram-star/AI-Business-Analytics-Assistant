from utils.date_filter import apply_date_filter
from utils.schema_interpreter import interpret_schema


def apply_business_filters(df, question):

    question = question.lower()
    schema = interpret_schema(df)
    # Date filter
    df = apply_date_filter(
        df,
        question,
        schema
    )

  
    

    print("Rows after business filter:", len(df))

    # COUNTRY
    country_col = schema.get("country")
    if country_col:
        for value in df[country_col].dropna().unique():
            if str(value).lower() in question:
                df = df[
                    df[country_col].astype(str).str.lower() == str(value).lower()
                ]
                print("Filtered Country:", value)
                print("Remaining Rows:", len(df))

    # PRODUCT
    product_col = schema.get("product")
    if product_col:
        for value in df[product_col].dropna().unique():
            if str(value).lower() in question:
                df = df[
                    df[product_col].astype(str).str.lower() == str(value).lower()
                ]

    # CUSTOMER
    customer_col = schema.get("customer")
    if customer_col:
        for value in df[customer_col].dropna().unique():
            if str(value).lower() in question:
                df = df[
                    df[customer_col].astype(str).str.lower() == str(value).lower()
                ]

    return df