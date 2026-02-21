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