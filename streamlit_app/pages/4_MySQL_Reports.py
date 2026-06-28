"""
==========================================================
MySQL Reports
==========================================================
"""

import streamlit as st

from utils.db_connection import load_data
from utils.load_css import load_css

from components.layout.footer import show_footer

from components.reports.header import (
    show_reports_header,
)

from components.reports.kpi_cards import (
    show_reports_kpis,
)

from components.reports.charts import (
    show_reports_charts,
)

from components.reports.insights import (
    show_reports_insights,
)

from components.reports.report_tables import (
    show_report_table,
)

from components.reports.export import (
    show_export_center,
)


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="MySQL Reports",

    page_icon="🗄️",

    layout="wide",

)

load_css()


# ==========================================================
# Load Reports
# ==========================================================

yearly_df = load_data(
    """
    SELECT *
    FROM crime_yearly_summary
    """
)

category_df = load_data(
    """
    SELECT *
    FROM crime_category_summary
    """
)

arrest_df = load_data(
    """
    SELECT *
    FROM vw_arrest_summary
    """
)

community_df = load_data(
    """
    SELECT

        community_code,

        COUNT(*) AS Crime_Count

    FROM crime

    GROUP BY community_code

    ORDER BY Crime_Count DESC
    """
)


# ==========================================================
# Header
# ==========================================================

show_reports_header()


# ==========================================================
# KPI Cards
# ==========================================================

show_reports_kpis(

    yearly_df,

    category_df,

)


# ==========================================================
# Charts
# ==========================================================

show_reports_charts(

    yearly_df,

    category_df,

    arrest_df,

    community_df,

)


# ==========================================================
# Insights
# ==========================================================

show_reports_insights(

    yearly_df,

    category_df,

)


# ==========================================================
# Report Selector
# ==========================================================

st.subheader("📋 SQL Report Tables")

report_option = st.selectbox(

    "Select Report",

    [

        "Yearly Crime Report",

        "Crime Category Report",

        "Yearly Arrest Report",

    ],

)

if report_option == "Yearly Crime Report":

    report_df = yearly_df

    sql_query = """
SELECT *
FROM crime_yearly_summary;
"""

    report_name = "Yearly Crime Report"

elif report_option == "Crime Category Report":

    report_df = category_df

    sql_query = """
SELECT *
FROM crime_category_summary;
"""

    report_name = "Crime Category Report"

else:

    report_df = arrest_df

    sql_query = """
SELECT *
FROM vw_arrest_summary;
"""

    report_name = "Yearly Arrest Report"


# ==========================================================
# Report Table
# ==========================================================

show_report_table(

    dataframe=report_df,

    report_name=report_name,

    sql_query=sql_query,

)


# ==========================================================
# Export Center
# ==========================================================

show_export_center(

    yearly_df=yearly_df,

    category_df=category_df,

    arrest_df=arrest_df,

    community_df=community_df,

    report_df=report_df,

    report_name=report_name.lower().replace(" ", "_"),

)


# ==========================================================
# Footer
# ==========================================================

show_footer()