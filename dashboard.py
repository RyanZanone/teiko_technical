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
st.markdown("Comparing the differences in cell population relative frequencies of _**melanoma**_ patients \
            receiving _**miraclib**_ who respond _**(responders)**_ versus those who do not _**(non-responders)**_. _**PBMC**_ samples ONLY.")

filtered_df = data_analysis.filter_data(summary_df)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Population Distributions")
    fig = data_analysis.generate_boxplots(filtered_df)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Differences in Relative Frequencies Between Responders and Non-Responders")
    st.markdown("Results of running independent T-tests comparing responders vs. non-responders for each cell population. Considered a significant difference if the p-value is less than 0.05")
    stats_df = data_analysis.run_statistical_tests(filtered_df)
    st.dataframe(stats_df, hide_index=True)

st.divider()

st.header("Data Subset Analysis")
st.markdown("Analysis of all _**melanoma PBMC**_ samples at _**baseline**_ (time_from_treatment_start is 0) for patients who have been treated with _**miraclib**_.")

project_counts, response_counts, sex_counts = data_analysis.get_baseline_subset()

col3, col4, col5 = st.columns(3)

with col3:
    st.subheader("Samples per Project")
    st.dataframe(project_counts, hide_index=True, use_container_width=True)

with col4:
    st.subheader("Subjects by Response")
    st.dataframe(response_counts, hide_index=True, use_container_width=True)

with col5:
    st.subheader("Subjects by Sex")
    st.dataframe(sex_counts, hide_index=True, use_container_width=True)