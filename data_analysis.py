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