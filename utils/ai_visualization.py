import plotly.express as px

def generate_chart_from_prompt(prompt, df):

    prompt = prompt.lower()

    if "sales" in prompt and "country" in prompt:

        country_col = next(
            (c for c in df.columns if "country" in c.lower()),
            None
        )

        sales_col = next(
            (c for c in df.columns if "sales" in c.lower()),
            None
        )

        if country_col and sales_col:
            summary = (
                df.groupby(country_col)[sales_col]
                .sum()
                .reset_index()
            )

            fig = px.bar(
                summary,
                x=country_col,
                y=sales_col,
                title="Sales by Country"
            )

            return fig, "Showing total sales by country."

    return None, "I couldn't generate a chart for that request yet."