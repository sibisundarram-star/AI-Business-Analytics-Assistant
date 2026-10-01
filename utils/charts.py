import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def show_missing_values(df):

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    if missing.empty:
        st.success("No missing values found.")
        return

    fig, ax = plt.subplots(figsize=(8,4))

    missing.sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_xlabel("Missing Values")
    ax.set_ylabel("Columns")

    st.pyplot(fig)