import streamlit as st
import plotly.express as px


def visualization_studio(df):

    st.subheader("📊 Visualization Studio")

    numeric = df.select_dtypes(include="number").columns.tolist()
    categorical = df.select_dtypes(exclude="number").columns.tolist()

    chart = st.selectbox(
        "Chart Type",
        [
            "Bar Chart",
            "Line Chart",
            "Scatter Plot",
            "Histogram",
            "Box Plot",
            "Pie Chart"
        ]
    )

    x = st.selectbox("X Axis", df.columns)

    y = None

    if chart != "Pie Chart":
        y = st.selectbox("Y Axis", numeric)

    if st.button("Generate Chart"):

        fig = None

        if chart == "Bar Chart":
            fig = px.bar(df, x=x, y=y)

        elif chart == "Line Chart":
            fig = px.line(df, x=x, y=y)

        elif chart == "Scatter Plot":
            fig = px.scatter(df, x=x, y=y)

        elif chart == "Histogram":
            fig = px.histogram(df, x=x)

        elif chart == "Box Plot":
            fig = px.box(df, x=x, y=y)

        elif chart == "Pie Chart":

            if x in categorical:

                counts = df[x].value_counts().reset_index()
                counts.columns = [x, "Count"]

                fig = px.pie(
                    counts,
                    names=x,
                    values="Count"
                )

            else:
                st.warning("Pie charts require a categorical column.")

        if fig:
            st.plotly_chart(fig, width="stretch")