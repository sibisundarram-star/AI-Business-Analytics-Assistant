import profile

import pandas as pd

def extract_metadata(df):

    metadata = {
        "rows": len(df),
        "columns": list(map(str, df.columns)),
        "dtypes": {
            str(col): str(df[col].dtype)
            for col in df.columns
        },
        "sample": df.head(5).to_dict(orient="records")
    }

    return metadata
def build_prompt(metadata):

    prompt = f"""
You are a senior Business Intelligence Analyst.

Analyse this dataset.

Dataset Metadata:

Rows:
{metadata["rows"]}

Columns:
{metadata["columns"]}

Data Types:
{metadata["dtypes"]}

Sample Data:
{metadata["sample"]}

Return ONLY JSON with:

- domain
- dataset_type
- primary_kpis
- dimensions
- time_columns
- recommended_visuals
- business_questions
- summary

Do not explain anything outside JSON.
"""

    return prompt
def generate_profile(df):

    metadata = extract_metadata(df)

    prompt = build_prompt(metadata)

    # Call AI here

    return profile
def generate_profile(df):

    metadata = extract_metadata(df)

    prompt = build_prompt(metadata)

    # Temporary output
    return {
        "metadata": metadata,
        "prompt": prompt
    }