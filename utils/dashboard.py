import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
def show_dashboard(df):

    st.markdown("## 📊 Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        show_missing_chart(df)

    with col2:
        show_datatype_chart(df)
def show_missing_chart(df):

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    if missing.empty:
        st.success("No missing values.")
        return

    fig, ax = plt.subplots(figsize=(6,4))

    missing.sort_values().plot.barh(ax=ax)

    ax.set_title("Missing Values")

    st.pyplot(fig)
def show_datatype_chart(df):
    numeric = len(df.select_dtypes(include="number").columns)
    categorical = len(df.select_dtypes(include=["object", "category"]).columns)
    fig, ax = plt.subplots(figsize=(5,5))
    ax.pie(
        [numeric, categorical],
        labels=["Numeric", "Categorical"],
        autopct="%1.1f%%",
        startangle=90
    )
    ax.set_title("Column Types")
    st.pyplot(fig)