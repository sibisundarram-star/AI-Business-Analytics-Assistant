import pandas as pd
import streamlit as st


@st.cache_data
def load_data(uploaded_file):
    """
    Load a CSV or Excel file into a pandas DataFrame.
    """

    if uploaded_file is None:
        return None

    file_name = uploaded_file.name.lower()

    try:
        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif file_name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)

        else:
            st.error("Unsupported file format.")
            return None

        return df

    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None