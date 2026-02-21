import sqlite3
import pandas as pd
from scipy import stats
import plotly.express as px

PATH_TO_DB = "clinical_trial.db"

def summary_table():
    conn = sqlite3.connect(PATH_TO_DB)
    query = "SELECT sample_id AS sample, population, count FROM CellCounts"
    df = pd.read_sql(query, conn)
    conn.close()

    total_counts = df.groupby("sample")["count"].sum().reset_index()
    total_counts.rename(columns={"count": "total_count"}, inplace=True)

    summary_df = pd.merge(df, total_counts, on="sample")
    summary_df["percentage"] = (summary_df["count"] / summary_df["total_count"]) * 100

    return summary_df[["sample", "total_count", "population", "count", "percentage"]]

def filter_data(summary_df):
    conn = sqlite3.connect(PATH_TO_DB)
    query = """
        SELECT Samples.sample_id AS sample, Subjects.condition, Samples.treatment, Samples.sample_type, Samples.response
        FROM Samples
        JOIN Subjects ON Samples.subject_id = Subjects.subject_id
        WHERE Subjects.condition = 'melanoma'
            AND Samples.treatment = 'miraclib'
            AND Samples.sample_type = 'PBMC'
            AND Samples.response IN ('yes', 'no')
    """

    filtered_df = pd.read_sql(query, conn)
    conn.close()

    return pd.merge(filtered_df, summary_df, on="sample")

def generate_boxplots(df):
    fig = px.box(
        df, x="population", y="percentage", color="response",
        title="Cell Population Relative Frequencies: Responders vs Non-Responders",
        labels={"percentage": "Relative Frequency (%)", "population": "Immune Cell Population"},
        color_discrete_map={"yes": "green", "no": "red"}
    )
    return fig

def run_statistical_tests(df):
    populations = df["population"].unique()
    results = []

    for pop in populations:
        pop_data = df[df["population"] == pop]
        responders = pop_data[pop_data["response"] == "yes"]["percentage"]
        non_responders = pop_data[pop_data["response"] == "no"]["percentage"]

        t_stat, p_val = stats.ttest_ind(responders, non_responders, equal_var=False)
        significat = "Yes" if p_val < 0.05 else "No"

        results.append({
            "Cell Population": pop,
            "P-Value": p_val,
            "Significant Difference? (p < 0.05)": significat
        })

    return pd.DataFrame(results)