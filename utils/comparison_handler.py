import pandas as pd

def compare_entities(df, schema, entity1, entity2):
    
    country_col = schema["country"]
    sales_col = schema["sales"]

    comparison_df = (
        df[
            df[country_col]
            .astype(str)
            .str.lower()
            .isin([
                entity1.lower(),
                entity2.lower()
            ])
        ]
        .groupby(country_col)[sales_col]
        .sum()
        .reset_index()
    )

    return comparison_df