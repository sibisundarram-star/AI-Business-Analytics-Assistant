import streamlit as st
from utils.data_loader import load_data
from utils.analyser import get_dataset_overview
from utils.insights import generate_insights
from utils.ai_engine import ask_ai
from utils.chart_generator import *
from utils.exporter import export_csv, export_excel
from utils.report_generator import generate_pdf

st.set_page_config(
    page_title="AI Business Analytics Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Analytics Assistant")
st.divider()

# Upload Dataset
st.header("Upload Dataset")
uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx"]
)
df = load_data(uploaded_file)

if uploaded_file is not None:
    df = load_data(uploaded_file)
    if df is not None:
        st.success("Dataset loaded successfully!")
        
st.divider()

# Dataset Overview
st.header("Dataset Overview")
if df is not None:

    overview = get_dataset_overview(df)

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Rows", overview["rows"])
    col2.metric("Columns", overview["columns"])
    col3.metric("Missing Values", overview["missing"])
    col4.metric("Duplicates", overview["duplicates"])
    col5.metric("Memory (MB)", overview["memory"])

st.divider()

# Data Preview
st.header("Data Preview")
if df is not None:

    preview_option = st.radio(
        "Rows to display",
        [5, 10, 20, 50],
        horizontal=True
    )

    st.dataframe(
        df.head(preview_option),
        use_container_width=True
    )

st.divider()

# Business Insights
st.header("Business Insights")
if df is not None:

    insights = generate_insights(df)

    for insight in insights:
        st.info(insight)

st.divider()

# AI Chat
st.header("AI Chat")
if df is not None:

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    question = st.chat_input("Ask a question about your dataset...")

    if question:

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Generate response
        response = ask_ai(question, df)

        # Save assistant message
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response["message"]
            }
        )

        with st.chat_message("assistant"):
            st.markdown(response["message"])

            if "table" in response and response["table"] is not None:
                st.dataframe(
                    response["table"],
                    use_container_width=True
                )
            if response["chart"] is not None:

                chart = response["chart"]

                if chart["type"] == "bar":
                    fig = create_bar_chart(
                        chart["data"],
                        chart["x"],
                        chart["y"]

                
                    )
                elif chart["type"] == "line":
                    fig = create_line_chart(
                        chart["data"],
                        chart["x"],
                        chart["y"]
                    )

                elif chart["type"] == "pie":
                    fig = create_pie_chart(
                        chart["data"],
                        chart["x"],
                        chart["y"]
                    )
                st.plotly_chart(fig, use_container_width=True)
st.divider()

# Visualization
st.header("Visualization")
if df is not None:

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    if numeric_columns and categorical_columns:

        col1, col2, col3 = st.columns(3)

        with col1:
            chart_type = st.selectbox(
                "Chart",
                ["Bar", "Line", "Pie"]
            )

        with col2:
            x_axis = st.selectbox(
                "Category",
                categorical_columns
            )

        with col3:
            y_axis = st.selectbox(
                "Value",
                numeric_columns
            )

        summary = (
            df.groupby(x_axis)[y_axis]
            .sum()
            .reset_index()
        )

        if chart_type == "Bar":
            fig = create_bar_chart(summary, x_axis, y_axis)

        elif chart_type == "Line":
            fig = create_line_chart(summary, x_axis, y_axis)

        else:
            fig = create_pie_chart(summary, x_axis, y_axis)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.divider()

# Export
st.header("Export")
if df is not None:
    overview = get_dataset_overview(df)
    insights = generate_insights(df)

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="📄 Download CSV",
            data=export_csv(df),
            file_name="dataset.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col2:

        st.download_button(
            label="📊 Download Excel",
            data=export_excel(df),
            file_name="dataset.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

    with col3:
        st.download_button(
            "📑 Download PDF Report",
            generate_pdf(overview, insights),
            "Business_Report.pdf",
            "application/pdf",
            use_container_width=True
        )