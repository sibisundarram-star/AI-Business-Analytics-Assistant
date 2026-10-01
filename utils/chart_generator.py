import plotly.express as px
import pandas as pd


def create_bar_chart(df, x, y):
    fig = px.bar(
        df,
        x=x,
        y=y,
        title=f"{y} by {x}"
    )

    return fig


def create_line_chart(df, x, y):
    fig = px.line(
        df,
        x=x,
        y=y,
        title=f"{y} by {x}"
    )

    return fig


def create_pie_chart(df, names, values):
    fig = px.pie(
        df,
        names=names,
        values=values,
        title=f"{values} by {names}"
    )

    return fig