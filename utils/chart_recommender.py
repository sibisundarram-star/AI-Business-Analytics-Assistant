import pandas as pd


def recommend_best_chart(df):

    numeric = df.select_dtypes(include="number").columns.tolist()
    categorical = df.select_dtypes(exclude="number").columns.tolist()

    recommendations = []

    if len(categorical) >= 1 and len(numeric) >= 1:
        recommendations.append({
            "title": "Category Comparison",
            "chart": "Bar Chart",
            "x": categorical[0],
            "y": numeric[0]
        })

    if len(numeric) >= 2:
        recommendations.append({
            "title": "Relationship Analysis",
            "chart": "Scatter Plot",
            "x": numeric[0],
            "y": numeric[1]
        })

    if len(numeric) >= 1:
        recommendations.append({
            "title": "Distribution",
            "chart": "Histogram",
            "x": numeric[0]
        })

    return recommendations