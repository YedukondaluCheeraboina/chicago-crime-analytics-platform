"""
==========================================================
Crime Category Analysis
==========================================================
"""

import streamlit as st
import pandas as pd

from components.charts.bar_chart import create_bar_chart
from components.charts.donut_chart import create_donut_chart


# ==========================================================
# Prepare Data
# ==========================================================

def prepare_category_data(filtered_df, top_n=10):

    category_df = (
        filtered_df["primary_type"]
        .value_counts()
        .head(top_n)
        .reset_index()
    )

    category_df.columns = [
        "Crime Type",
        "Crime Count",
    ]

    category_df.insert(
        0,
        "Rank",
        range(1, len(category_df) + 1),
    )

    total = category_df["Crime Count"].sum()

    category_df["Percentage"] = (
        category_df["Crime Count"] / total * 100
    ).round(2)

    return category_df


# ==========================================================
# Category Chart
# ==========================================================

def show_category_chart(filtered_df):

    category_df = prepare_category_data(filtered_df)

    left, right = st.columns(2)

    with left:

        st.subheader("📊 Crime Distribution")

        fig = create_bar_chart(

            dataframe=category_df,

            x="Crime Type",

            y="Crime Count",

            color="#3B82F6",

        )

        st.plotly_chart(

            fig,

            use_container_width=True,

        )

    with right:

        st.subheader("🟠 Category Share")

        fig = create_donut_chart(

            dataframe=category_df,

            names="Crime Type",

            values="Crime Count",

        )

        st.plotly_chart(

            fig,

            use_container_width=True,

        )


# ==========================================================
# Category Table
# ==========================================================

def show_category_table(filtered_df):

    category_df = prepare_category_data(filtered_df)

    st.subheader("📋 Top Crime Categories")

    st.dataframe(

        category_df,

        hide_index=True,

        use_container_width=True,

        height=340,

    )


# ==========================================================
# Category Insights
# ==========================================================

def show_category_insights(filtered_df):

    category_df = prepare_category_data(filtered_df)

    top = category_df.iloc[0]

    with st.container(border=True):

        st.subheader("📂 Crime Insights")

        st.metric(

            "Top Crime",

            top["Crime Type"],

        )

        st.metric(

            "Crime Count",

            f"{top['Crime Count']:,}",

        )

        st.metric(

            "Contribution",

            f"{top['Percentage']}%",

        )

        st.divider()

        st.info(

            "Increase patrol deployment for the highest occurring crime category."

        )