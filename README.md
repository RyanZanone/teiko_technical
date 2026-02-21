# Ryan Zanone Teiko Technical Exam

## Instructions
- Dependencies can be found in `requirements.txt`
- To run the data loading script, simply run `python load_data.py`
- To run the dashboard application, run `streamlit run dashboard.py`

## Schema Design
I decided to structure our database with 3 distinct tables, **Subjects**, **Samples** and **CellCounts**. 
- **Subjects**: This table is meant for storing individual subject data. With the current csv format, multiple rows can correspond to the same subject as different samples are taken from them. Because of this, there is a lot of redundant, duplicate data being stored for things like the subject's sex, age, etc., which can present major issues as we scale. By creating a separate Subjects table, we are able to have one entry per subject to access all of their static data.
- **Samples**: Here, individual samples reference subjects from the subject table, meaning we don't have to store that subject specific data for every single sample that we collect, as we can collect many samples from just one individual subject. It also allows for samples to be collected from the same subject under different circumstances, like at a different time interval, with different treatment, or a different response. This allows us to easily add samples while only adding necessary information for that sample.
- **CellCounts**: Here, the major change I decided to make was changing to a "wide" to a "long" data format to allow for better scalability. Instead of every cell type having its own column, we simply have a row refer to the population of a single cell type for a given sample. This helps scale for future analytics we'd like to gather because if we want to add new cell types to analyze, we would just have to insert new rows rather than alter the entire schema and add new columns.

## Code Structure/Design
My main goal in structuring my code was keeping things organized, and easy to expand on. We have a separate `db_schema.sql` file that can be easily updated if we want to add additional tables or completely overhaul the schema itself (although `load_data.py` would need to be run again). I separated the generation of the user-facing aspects of the dashboard and the functions that perform the statistical analysis and data processing into two different files (like separating a frontend and backend for any other application). This allows the dashboard to directly call any service it may need from the `data_analysis.py` module, and lets the developer add additional functionality easily, and in an organized manner. Each function handles a separate concern, and they're all separated into fairly small, isolated tasks (like running a specific query, then performing some math or statistical tests on the data obtained from that query), which keeps functions easy to understand and not extending their scope too far. Also, for the statistical tests in Part 3, I decided to use Welch's T-Test because we have unequal sample sizes and variance, and are comparing only 2 independent groups.

_**NOTE:**_ I was a bit confused by the final question in the Google Form, as I wasn't entirely sure if you wanted this value derived from the subset of data mentioned in Part 4, or from the entire dataset. I included both values on the dashboard, but the answer in the Google Form is for the **entire** dataset.

Here is the link to my dashboard: https://ryanzanone-teikotechnical-dashboard.streamlit.app/

