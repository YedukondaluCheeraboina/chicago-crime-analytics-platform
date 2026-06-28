"""
==========================================================
Statistical Analysis
==========================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.db_connection import load_crime_data
from components.layout.sidebar import show_sidebar
from components.layout.footer import show_footer
# from datetime import datetime
from utils.load_css import load_css

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Statistical Analysis",
    page_icon="📈",
    layout="wide"
)

# Load Custom CSS
load_css()


# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

crime_df = load_crime_data()

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

(
    selected_year,
    selected_crime,
    top_n,
    sort_order
) = show_sidebar(crime_df)

# ----------------------------------------------------------
# Apply Filters
# ----------------------------------------------------------

filtered_df = crime_df.copy()

if selected_year != "All":
    filtered_df = filtered_df[
        filtered_df["Year"] == selected_year
    ]

if selected_crime != "All":
    filtered_df = filtered_df[
        filtered_df["primary_type"] == selected_crime
    ]

if filtered_df.empty:

    st.warning("No records available.")

    st.stop()

# ----------------------------------------------------------
# Page Header
# ----------------------------------------------------------

st.title("📈 Statistical Analysis")

st.caption(
    "Statistical insights and pattern detection for Chicago crime data."
)

st.markdown("---")

st.markdown("## 📊 Statistical Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Records",
        f"{len(filtered_df):,}"
    )

with col2:

    st.metric(
        "Crime Types",
        filtered_df["primary_type"].nunique()
    )

with col3:

    st.metric(
        "Communities",
        filtered_df["community_code"].nunique()
    )

with col4:

    st.metric(
        "Average Crimes / Hour",
        round(
            filtered_df.groupby("Hour")
            .size()
            .mean(),
            2
        )
    )

# ==========================================================
# Crime Intensity by Hour
# ==========================================================

st.markdown("---")

left_col, right_col = st.columns(2)

with left_col:

    st.subheader("📈 Crime Intensity by Hour")

    hour_summary = (
        filtered_df.groupby("Hour")
        .size()
        .reset_index(name="Crime_Count")
    )

    fig1 = px.line(

        hour_summary,

        x="Hour",

        y="Crime_Count",

        markers=True,

        title="Crime Intensity Throughout the Day"

    )

    fig1.update_layout(

        template="plotly_white",

        height=450,

        xaxis_title="Hour",

        yaxis_title="Crime Count"

    )

    st.plotly_chart(
        fig1,
        width="stretch"
    )

with right_col:

    st.subheader("📦 Community Area Outliers")

    community_summary = (
        filtered_df.groupby("community_code")
        .size()
        .reset_index(name="Crime_Count")
    )

    fig2 = px.box(

        community_summary,

        y="Crime_Count",

        points="all",

        title="Crime Distribution Across Communities"

    )

    fig2.update_layout(

        template="plotly_white",

        height=450,

        yaxis_title="Crime Count"

    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )


# ==========================================================
# Second Row
# ==========================================================

st.markdown("---")

left_col2, right_col2 = st.columns(2)

with left_col2:

    st.subheader("📊 Hourly Crime Distribution")

    fig3 = px.histogram(

        filtered_df,

        x="Hour",

        nbins=24,

        title="Crime Distribution by Hour"

    )

    fig3.update_layout(

        template="plotly_white",

        height=450,

        xaxis_title="Hour of Day",

        yaxis_title="Crime Frequency"

    )

    st.plotly_chart(

        fig3,

        width="stretch"

    )

with right_col2:

    st.subheader("🏘️ Community Crime Distribution")

    community_distribution = (

        filtered_df

        .groupby("community_code")

        .size()

        .reset_index(name="Crime_Count")

        .sort_values(

            by="Crime_Count",

            ascending=False

        )

        .head(10)

    )

    fig4 = px.bar(

        community_distribution,

        x="community_code",

        y="Crime_Count",

        color="Crime_Count",

        text="Crime_Count",

        title="Top 10 Community Areas"

    )

    fig4.update_traces(

        textposition="outside"

    )

    fig4.update_layout(

        template="plotly_white",

        height=450,

        xaxis_title="Community Area",

        yaxis_title="Crime Count",

        showlegend=False

    )

    st.plotly_chart(

        fig4,

        width="stretch"

    )


# ==========================================================
# Statistical Insights
# ==========================================================

st.markdown("---")

st.subheader("💡 Statistical Insights")

insight_col1, insight_col2 = st.columns(2)

with insight_col1:

    peak_hour = hour_summary.loc[
        hour_summary["Crime_Count"].idxmax()
    ]

    average_crime = round(
        hour_summary["Crime_Count"].mean(),
        2
    )

    st.info(

        f"""
### 📈 Statistical Summary

• Peak Crime Hour:
**{int(peak_hour['Hour'])}:00**

• Crimes During Peak Hour:
**{peak_hour['Crime_Count']}**

• Average Crimes per Hour:
**{average_crime}**
"""

    )

with insight_col2:

    highest_area = community_summary.loc[
        community_summary["Crime_Count"].idxmax()
    ]

    st.success(

        f"""
### 🚔 Business Observation

• Highest Crime Community:
**{int(highest_area['community_code'])}**

• Crimes Recorded:
**{highest_area['Crime_Count']}**

• Recommendation:

Increase police deployment in
high crime community areas.
"""

    )

st.markdown("---")

st.subheader("📋 Statistical Summary")

statistics = pd.DataFrame({

    "Statistic":[

        "Total Records",

        "Crime Categories",

        "Community Areas",

        "Average Crimes / Hour",

        "Peak Crime Hour"

    ],

    "Value":[

        len(filtered_df),

        filtered_df["primary_type"].nunique(),

        filtered_df["community_code"].nunique(),

        round(
            hour_summary["Crime_Count"].mean(),
            2
        ),

        int(
            peak_hour["Hour"]
        )

    ]

})

st.dataframe(

    statistics,

    width="stretch",

    hide_index=True

)


csv = statistics.to_csv(
    index=False
).encode("utf-8")

st.download_button(

    "📥 Download Statistical Summary",

    csv,

    file_name="statistical_summary.csv",

    mime="text/csv"

)


show_footer()