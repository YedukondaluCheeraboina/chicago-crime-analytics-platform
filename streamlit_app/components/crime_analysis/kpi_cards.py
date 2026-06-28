"""
==========================================================
Crime Analysis KPI Cards
==========================================================
"""

import streamlit as st

from components.common.card import metric_card


def show_crime_analysis_kpis(filtered_df):
    """
    Display Crime Analysis KPI Cards.
    """

    total_crimes = len(filtered_df)

    crime_categories = filtered_df["primary_type"].nunique()

    communities = filtered_df["community_code"].nunique()

    districts = filtered_df["district_code"].nunique()

    if total_crimes > 0:
        top_crime = (
            filtered_df["primary_type"]
            .value_counts()
            .idxmax()
        )
    else:
        top_crime = "N/A"

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        metric_card(
            title="Total Crimes",
            value=f"{total_crimes:,}",
            subtitle="Filtered Records",
            icon="🚔",
            accent_color="#2563EB",
        )

    with col2:

        metric_card(
            title="Top Crime",
            value=top_crime,
            subtitle="Most Frequent Crime",
            icon="🏆",
            accent_color="#EF4444",
        )

    with col3:

        metric_card(
            title="Crime Types",
            value=crime_categories,
            subtitle="Unique Categories",
            icon="📂",
            accent_color="#10B981",
        )

    with col4:

        metric_card(
            title="Communities",
            value=communities,
            subtitle="Affected Areas",
            icon="🏘",
            accent_color="#8B5CF6",
        )