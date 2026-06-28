"""
==========================================================
MySQL Report Query Cards
==========================================================
Project : Chicago Crime Analytics
==========================================================
"""

import streamlit as st


# ==========================================================
# Query Card
# ==========================================================

def _query_card(title: str, description: str):

    with st.container(border=True):

        st.subheader(title)

        st.caption(description)

        st.button(
            "View Report",
            use_container_width=True,
            disabled=True,
        )


# ==========================================================
# Query Dashboard
# ==========================================================

def show_query_cards():

    st.subheader("📊 Available SQL Reports")

    st.caption(
        "Browse predefined reports generated using SQL queries."
    )

    col1, col2 = st.columns(2)

    with col1:

        _query_card(

            "🚔 Crime by Type",

            "Distribution of crimes grouped by primary crime type.",

        )

        _query_card(

            "🏢 Crime by District",

            "Top districts with the highest reported crimes.",

        )

        _query_card(

            "📅 Monthly Crime Trend",

            "Monthly trend analysis of reported crimes.",

        )

        _query_card(

            "🕒 Hourly Crime Pattern",

            "Crime occurrences across different hours of the day.",

        )

    with col2:

        _query_card(

            "🚓 Arrest Analysis",

            "Arrest rate and arrest distribution analysis.",

        )

        _query_card(

            "🏘 Community Analysis",

            "Crime statistics by community area.",

        )

        _query_card(

            "🏠 Domestic Crime",

            "Domestic crime incidents and patterns.",

        )

        _query_card(

            "📍 Beat Analysis",

            "Crime analysis by police beat.",

        )

    st.divider()