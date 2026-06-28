"""
==========================================================
MySQL Report Tables
==========================================================
Project : Chicago Crime Analytics
==========================================================
"""

import streamlit as st
import pandas as pd


# ==========================================================
# Report Table
# ==========================================================

def show_report_table(
    dataframe: pd.DataFrame,
    report_name: str,
    sql_query: str,
):
    """
    Display a SQL report table with metadata.
    """

    st.subheader(f"📄 {report_name}")

    with st.expander("📝 SQL Query", expanded=False):

        st.code(
            sql_query,
            language="sql",
        )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Rows Returned",

            len(dataframe),

        )

    with col2:

        st.metric(

            "Columns",

            len(dataframe.columns),

        )

    with col3:

        st.metric(

            "Status",

            "Success",

        )

    st.dataframe(

        dataframe,

        hide_index=True,

        use_container_width=True,

        height=450,

    )

    st.caption(

        f"Displaying {len(dataframe):,} record(s)."

    )

    st.divider()


# ==========================================================
# Empty Report
# ==========================================================

def show_empty_report():

    st.info(

        "Select a report to display SQL query results."

    )