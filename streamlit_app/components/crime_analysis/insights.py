"""
==========================================================
Crime Analysis - Business Insights
==========================================================
"""

import streamlit as st


# ==========================================================
# Prepare Insights
# ==========================================================

def prepare_insights(filtered_df):

    total_crimes = len(filtered_df)

    top_crime = (

        filtered_df["primary_type"]

        .value_counts()

        .idxmax()

    )

    top_crime_count = (

        filtered_df["primary_type"]

        .value_counts()

        .max()

    )

    top_district = (

        filtered_df["district_code"]

        .value_counts()

        .idxmax()

    )

    top_district_count = (

        filtered_df["district_code"]

        .value_counts()

        .max()

    )

    arrest_rate = (

        filtered_df["arrest"]

        .mean()

        * 100

    )

    domestic_rate = (

        filtered_df["domestic"]

        .mean()

        * 100

    )

    return {

        "total_crimes": total_crimes,

        "top_crime": top_crime,

        "top_crime_count": top_crime_count,

        "top_district": top_district,

        "top_district_count": top_district_count,

        "arrest_rate": arrest_rate,

        "domestic_rate": domestic_rate,

    }


# ==========================================================
# Executive Insight Card
# ==========================================================

def show_executive_insights(filtered_df):

    insights = prepare_insights(filtered_df)

    with st.container(border=True):

        st.subheader("📈 Executive Insights")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Total Crimes",

                f"{insights['total_crimes']:,}"

            )

            st.metric(

                "Top Crime",

                insights["top_crime"]

            )

            st.metric(

                "Crime Count",

                f"{insights['top_crime_count']:,}"

            )

        with col2:

            st.metric(

                "Top District",

                insights["top_district"]

            )

            st.metric(

                "District Crimes",

                f"{insights['top_district_count']:,}"

            )

            st.metric(

                "Arrest Rate",

                f"{insights['arrest_rate']:.2f}%"

            )


# ==========================================================
# Pattern Insight Card
# ==========================================================

def show_pattern_insights(filtered_df):

    insights = prepare_insights(filtered_df)

    with st.container(border=True):

        st.subheader("🔍 Crime Pattern Analysis")

        st.metric(

            "Domestic Crime Rate",

            f"{insights['domestic_rate']:.2f}%"

        )

        st.divider()

        st.success(

            "Deploy additional patrol units "

            "to the highest crime district."

        )

        st.info(

            "Focus preventive policing on "

            f"{insights['top_crime']} incidents."

        )

        st.warning(

            "Monitor seasonal crime patterns "

            "using the monthly trend analysis."

        )


# ==========================================================
# Dashboard Layout
# ==========================================================

def show_business_insights(filtered_df):

    left, right = st.columns(2)

    with left:

        show_executive_insights(filtered_df)

    with right:

        show_pattern_insights(filtered_df)