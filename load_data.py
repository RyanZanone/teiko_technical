import pandas as pd
import sqlite3
import os

def load_data():
    path_to_db = "clinical_trial.db"
    if os.path.exists(path_to_db):
        os.remove(path_to_db)

    conn = sqlite3.connect(path_to_db)
    cursor = conn.cursor()

    with open("db_schema.sql", "r") as f:
        schema_script = f.read()

    cursor.executescript(schema_script)

    df = pd.read_csv("cell-count.csv")

    subjects_df = df[["subject", "project", "condition", "age", "sex"]].drop_duplicates().rename(columns={"subject": "subject_id"})
    subjects_df.to_sql("Subjects", conn, if_exists="append", index=False)

    samples_df = df[["sample", "subject", "sample_type", "time_from_treatment_start", "treatment", "response"]].rename(columns={"sample": "sample_id", "subject" : "subject_id"})
    samples_df.to_sql("Samples", conn, if_exists="append", index=False)

    cell_count_cols = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]
    cell_counts_df = df.melt(id_vars=["sample"], value_vars=cell_count_cols, var_name="population", value_name="count").rename(columns={"sample": "sample_id"})
    cell_counts_df.to_sql("CellCounts", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()
    print("Loaded data from cell-count.csv into clinical_trial.db")

if __name__ == "__main__":
    load_data()