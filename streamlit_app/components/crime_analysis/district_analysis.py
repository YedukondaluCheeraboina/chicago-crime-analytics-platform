"""
==========================================================
District Analysis
==========================================================
"""

import streamlit as st
import pandas as pd

from components.charts.bar_chart import create_bar_chart


# ==========================================================
# Prepare Data
# ==========================================================

def prepare_district_data(filtered_df, top_n=10):

    district_df = (

        filtered_df

        .groupby("district_code")

        .size()

        .reset_index(name="Crime Count")

        .sort_values(

            by="Crime Count",

            ascending=False

        )

        .head(top_n)

        .reset_index(drop=True)

    )

    district_df.rename(

        columns={

            "district_code": "District"

        },

        inplace=True,

    )

    district_df.insert(

        0,

        "Rank",

        range(1, len(district_df) + 1),

    )

    total = district_df["Crime Count"].sum()

    district_df["Percentage"] = (

        district_df["Crime Count"]

        / total

        * 100

    ).round(2)

    return district_df


# ==========================================================
# District Chart
# ==========================================================

def show_district_chart(filtered_df):

    district_df = prepare_district_data(filtered_df)

    st.subheader("🏢 Crime by District")

    fig = create_bar_chart(

        dataframe=district_df,

        x="District",

        y="Crime Count",

        color="#8B5CF6",

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


# ==========================================================
# District Table
# ==========================================================

def show_district_table(filtered_df):

    district_df = prepare_district_data(filtered_df)

    st.subheader("📋 Top Districts")

    st.dataframe(

        district_df,

        hide_index=True,

        use_container_width=True,

        height=340,

    )


# ==========================================================
# District Insights
# ==========================================================

def show_district_insights(filtered_df):

    district_df = prepare_district_data(filtered_df)

    highest = district_df.iloc[0]

    lowest = district_df.iloc[-1]

    average = round(

        district_df["Crime Count"].mean(),

        1,

    )

    with st.container(border=True):

        st.subheader("🏢 District Insights")

        st.metric(

            "Highest District",

            highest["District"],

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

            f"Lowest : District {lowest['District']}"

        )

        st.divider()

        st.success(

            "Increase patrol strength in high-crime districts."

        )