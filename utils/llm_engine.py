import os
import json
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")


def get_client():
    """
    Create an OpenAI client using the API key from .env.
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured.")

    return OpenAI(api_key=api_key)


def build_dataset_context(df):
    """
    Build a compact description of the dataframe for the LLM.

    We do NOT send the entire dataset to the LLM.
    The LLM only receives the structure and limited examples.
    Pandas remains responsible for actual calculations.
    """

    context = {
        "rows": len(df),
        "columns": []
    }

    for column in df.columns:

        series = df[column]

        column_info = {
            "name": str(column),
            "dtype": str(series.dtype),
            "missing_values": int(series.isna().sum())
        }

        # Give the LLM a few representative values
        sample_values = (
            series.dropna()
            .astype(str)
            .drop_duplicates()
            .head(10)
            .tolist()
        )

        column_info["sample_values"] = sample_values

        if pd.api.types.is_numeric_dtype(series):

            numeric_series = pd.to_numeric(
                series,
                errors="coerce"
            ).dropna()

            if not numeric_series.empty:

                column_info["min"] = float(numeric_series.min())
                column_info["max"] = float(numeric_series.max())
                column_info["mean"] = float(numeric_series.mean())

        context["columns"].append(column_info)

    return context


def create_analysis_plan(question, df):
    """
    Ask the LLM to convert a natural-language business question
    into a structured analytical plan.

    The LLM interprets the question.
    Pandas performs the actual calculation.
    """

    client = get_client()

    dataset_context = build_dataset_context(df)

    system_prompt = """
You are an AI business analytics assistant.

Your job is to understand a user's business question about a pandas
DataFrame and convert it into a structured analytical plan.

IMPORTANT RULES:

1. Never invent numerical results.
2. Never calculate results yourself.
3. Pandas will perform the actual calculation.
4. Only reference columns that actually exist in the dataset.
5. Interpret natural business language.
6. Understand concepts such as:
   - open job cards
   - closed job cards
   - ageing
   - workload
   - advisor performance
   - technician workload
   - status
   - totals
   - averages
   - counts
   - rankings
7. If the question cannot be answered from the available columns,
   explain what information is missing.
8. Prefer simple analytical operations.

Return ONLY valid JSON with this structure:

{
    "understood": true,
    "operation": "count | sum | average | minimum | maximum | group_by | top_n | filter | describe",
    "column": null,
    "group_by": null,
    "filters": [],
    "n": null,
    "explanation": "short explanation of what should be calculated"
}

For filters use:

[
    {
        "column": "column_name",
        "operator": "equals",
        "value": "value"
    }
]

For example, if the user asks:

"Which advisor has the most open job cards?"

and the dataset contains Status and Advisor columns,
the plan should conceptually be:

{
    "understood": true,
    "operation": "group_by",
    "column": null,
    "group_by": "Advisor",
    "filters": [
        {
            "column": "Status",
            "operator": "equals",
            "value": "Open"
        }
    ],
    "n": null,
    "explanation": "Count open job cards for each advisor and rank them."
}
"""

    user_prompt = f"""
DATASET CONTEXT:

{json.dumps(dataset_context, indent=2, default=str)}

USER QUESTION:

{question}
"""

    response = client.responses.create(
        model=MODEL,
        instructions=system_prompt,
        input=user_prompt
    )

    output = response.output_text.strip()

    # Remove accidental markdown fences if the model adds them
    if output.startswith("```"):
        output = output.replace("```json", "")
        output = output.replace("```", "")
        output = output.strip()

    return json.loads(output)