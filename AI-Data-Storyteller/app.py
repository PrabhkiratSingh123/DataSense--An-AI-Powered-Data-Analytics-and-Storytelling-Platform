import streamlit as st
import pandas as pd
from eda.summary import get_summary,get_statistical_summary,get_correlation_matrix,get_column_summary
from eda.visualisation import plot_histogram, plot_bar, plot_pie, plot_scatter, plot_line
from preprocessing.cleaner import clean_dataset
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
        st.write("statistical summary")
        st.write(get_statistical_summary(df))
        st.write("correlation matrix")
        st.write(get_correlation_matrix(df))
        st.write("column summary")
        st.write(get_column_summary(df))
    if st.button("clean dataset"):
        st.write(clean_dataset(df))
    if st.button("Visualisation"):
        st.write(plot_histogram(df))
        st.write(plot_bar(df))
        st.write(plot_pie(df))
        st.write(plot_scatter(df))
        st.write(plot_line(df))