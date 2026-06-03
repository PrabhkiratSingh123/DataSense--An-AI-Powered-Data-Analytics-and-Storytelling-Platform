import streamlit as st
import pandas as pd
from eda.summary import get_summary
from eda.visualisation import plot_histogram, plot_bar, plot_pie, plot_scatter, plot_line
from eda.profiling import generate_profile_report

st.title("AI Data Storyteller")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx", "json"]
)

if uploaded_file:
    
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_json(uploaded_file)

    st.success("Dataset Uploaded Successfully")
    if st.button("Show Dataset"):
        st.write(df)
    if st.button("Summary"):
        st.write(get_summary(df))
    if st.button("Generate Profile Report"):
        st.info("Generating report... this might take a moment.")
        report = generate_profile_report(df)
        import streamlit.components.v1 as components
        components.html(report.to_html(), height=1000, scrolling=True)
    if st.button("Visualisation"):
        st.write(plot_histogram(df))
        st.write(plot_bar(df))
        st.write(plot_pie(df))
        st.write(plot_scatter(df))
        st.write(plot_line(df))