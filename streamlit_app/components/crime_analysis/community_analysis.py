"""
==========================================================
Community Area Analysis
==========================================================
"""

import streamlit as st
import pandas as pd

from components.charts.bar_chart import create_bar_chart


# ==========================================================
# Prepare Data
# ==========================================================

def prepare_community_data(filtered_df, top_n=10):

    community_df = (

        filtered_df

        .groupby("community_code")

        .size()

        .reset_index(name="Crime Count")

        .sort_values(

            by="Crime Count",

            ascending=False,

        )

        .head(top_n)

        .reset_index(drop=True)

    )

    community_df.rename(

        columns={

            "community_code": "Community"

        },

        inplace=True,

    )

    community_df.insert(

        0,

        "Rank",

        range(1, len(community_df) + 1),

    )

    total = community_df["Crime Count"].sum()

    community_df["Percentage"] = (

        community_df["Crime Count"]

        / total

        * 100

    ).round(2)

    return community_df


# ==========================================================
# Community Chart
# ==========================================================

def show_community_chart(filtered_df):

    community_df = prepare_community_data(filtered_df)

    st.subheader("🏘 Crime by Community")

    fig = create_bar_chart(

        dataframe=community_df,

        x="Community",

        y="Crime Count",

        color="#10B981",

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


# ==========================================================
# Community Table
# ==========================================================

def show_community_table(filtered_df):

    community_df = prepare_community_data(filtered_df)

    st.subheader("📋 Top Communities")

    st.dataframe(

        community_df,

        hide_index=True,

        use_container_width=True,

        height=340,

    )


# ==========================================================
# Community Insights
# ==========================================================

def show_community_insights(filtered_df):

    community_df = prepare_community_data(filtered_df)

    highest = community_df.iloc[0]

    lowest = community_df.iloc[-1]

    average = round(

        community_df["Crime Count"].mean(),

        1,

    )

    with st.container(border=True):

        st.subheader("🏘 Community Insights")

        st.metric(

            "Highest Community",

            highest["Community"],

        )

        st.metric(

            "Crime Count",

            f"{highest['Crime Count']:,}",

        )

        st.metric(

            "Average",

            average,

        )

        st.caption(

            f"Lowest : Community {lowest['Community']}"

        )

        st.divider()

        st.success(

            "Strengthen surveillance and community policing in high-crime areas."

        )