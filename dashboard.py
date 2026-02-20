import streamlit as st
import data_analysis

st.set_page_config(page_title="Loblaw Bio Analytics", layout="wide")
st.title("Loblaw Bio: Clinical Trial Dashboard")
st.markdown("Analysis of immune cell populations and treatment responses")

st.divider()

st.header("Initial Analysis - Data Overview")
st.markdown("Summary table of the relative frequency of each cell population")

summary_df = data_analysis.summary_table()
st.dataframe(summary_df, use_container_width=True)

st.divider()

st.header("Statistical Analysis")
st.markdown("Filtered summary data for: **Melanoma | Miraclib | PBMC | Responders vs Non-Responders**")

filtered_df = data_analysis.filter_data(summary_df)

st.dataframe(filtered_df, use_container_width=True)