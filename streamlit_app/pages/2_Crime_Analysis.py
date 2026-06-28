"""
==========================================================
Crime Analysis
==========================================================
Project : Chicago Crime Analytics
==========================================================
"""

import streamlit as st

from utils.load_css import load_css
from utils.db_connection import load_crime_data

from components.layout.header import show_header
from components.layout.sidebar import show_sidebar
from components.layout.footer import show_footer

from components.crime_analysis.header import (
    show_crime_analysis_header,
)

from components.crime_analysis.kpi_cards import (
    show_crime_analysis_kpis,
)

from components.crime_analysis.category_analysis import (
    show_category_chart,
    show_category_table,
    show_category_insights,
)

from components.crime_analysis.district_analysis import (
    show_district_chart,
    show_district_table,
    show_district_insights,
)

from components.crime_analysis.community_analysis import (
    show_community_chart,
    show_community_table,
    show_community_insights,
)

from components.crime_analysis.monthly_analysis import (
    show_monthly_chart,
    show_monthly_table,
    show_monthly_insights,
)

from components.crime_analysis.heatmap import (
    show_heatmap,
)

from components.crime_analysis.insights import (
    show_business_insights,
)

from components.crime_analysis.recommendations import (
    show_recommendations,
)

from components.crime_analysis.export import (
    show_crime_export,
)


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="Crime Analysis",

    page_icon="🚔",

    layout="wide",

)

load_css()

show_header(

    "Crime Analysis",

    "Comprehensive Crime Intelligence Dashboard",

)


# ==========================================================
# Load Dataset
# ==========================================================

crime_df = load_crime_data()


# ==========================================================
# Sidebar Filters
# ==========================================================

(

    selected_year,

    selected_crime,

    top_n,

    sort_order,

) = show_sidebar(crime_df)


filtered_df = crime_df.copy()


if selected_year != "All":

    filtered_df = filtered_df[

        filtered_df["Year"] == selected_year

    ]


if selected_crime != "All":

    filtered_df = filtered_df[

        filtered_df["primary_type"] == selected_crime

    ]


# ==========================================================
# Page Header
# ==========================================================

show_crime_analysis_header()


# ==========================================================
# KPI Overview
# ==========================================================

show_crime_analysis_kpis(filtered_df)


# ==========================================================
# Crime Category Analysis
# ==========================================================

st.divider()

st.subheader("🚔 Crime Category Analysis")

left, right = st.columns([1, 1])

with left:

    show_category_table(filtered_df)

    st.markdown("")

    show_category_insights(filtered_df)

with right:

    show_category_chart(filtered_df)

# ==========================================================
# District & Community Analysis
# ==========================================================

st.divider()

st.subheader("🏢 District & Community Analysis")

district_col, community_col = st.columns(2)

# ----------------------------------------------------------
# District Section
# ----------------------------------------------------------

with district_col:

    show_district_chart(filtered_df)

    st.markdown("")

    table_col, insight_col = st.columns(2)

    with table_col:

        show_district_table(filtered_df)

    with insight_col:

        show_district_insights(filtered_df)


# ----------------------------------------------------------
# Community Section
# ----------------------------------------------------------

with community_col:

    show_community_chart(filtered_df)

    st.markdown("")

    table_col, insight_col = st.columns(2)

    with table_col:

        show_community_table(filtered_df)

    with insight_col:

        show_community_insights(filtered_df)


# ==========================================================
# Monthly Crime Analysis
# ==========================================================

st.divider()

st.subheader("📅 Monthly Crime Analysis")

monthly_left, monthly_right = st.columns(2)

with monthly_left:

    show_monthly_chart(filtered_df)

with monthly_right:

    show_monthly_table(filtered_df)

    st.markdown("")

    show_monthly_insights(filtered_df)


# ==========================================================
# Crime Hotspot Analysis
# ==========================================================

st.divider()

st.subheader("🗺 Crime Hotspot Analysis")

show_heatmap(filtered_df)

# ==========================================================
# Business Insights
# ==========================================================

st.divider()

st.subheader("📈 Business Insights")

show_business_insights(filtered_df)


# ==========================================================
# Recommendations
# ==========================================================

st.divider()

show_recommendations(filtered_df)


# ==========================================================
# Export Center
# ==========================================================

st.divider()

show_crime_export(filtered_df)


# ==========================================================
# Footer
# ==========================================================

show_footer()