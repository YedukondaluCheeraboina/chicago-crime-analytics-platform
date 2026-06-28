"""
==========================================================
MySQL Report KPI Cards
==========================================================
"""

import streamlit as st


def show_reports_kpis(

    yearly_df,

    category_df,

):

    total_years = yearly_df["Year"].nunique()

    total_records = int(

        yearly_df["Crime_Count"].sum()

    )

    total_categories = len(category_df)

    avg_arrest_rate = yearly_df["Arrest_Rate"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(

            "📅 Years",

            total_years,

        )

    with col2:

        st.metric(

            "🚔 Categories",

            total_categories,

        )

    with col3:

        st.metric(

            "🚨 Total Crimes",

            f"{total_records:,}",

        )

    with col4:

        st.metric(

            "👮 Avg Arrest Rate",

            f"{avg_arrest_rate:.2f}%",

        )

    st.divider()