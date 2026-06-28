"""
==========================================================
MySQL Reports Header
==========================================================
Project : Chicago Crime Analytics
==========================================================
"""

import streamlit as st


def show_reports_header():
    """
    Display the header section for the MySQL Reports page.
    """

    st.title("🗄️ MySQL Reports")

    st.caption(
        "Execute predefined SQL reports and explore crime statistics "
        "directly from the MySQL database."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            "📊 **15+ Reports**\n\n"
            "Ready-to-use SQL queries."
        )

    with col2:
        st.success(
            "⚡ **Live Database**\n\n"
            "Connected to MySQL."
        )

    with col3:
        st.warning(
            "📁 **Export Ready**\n\n"
            "CSV • Excel • PDF"
        )

    st.divider()