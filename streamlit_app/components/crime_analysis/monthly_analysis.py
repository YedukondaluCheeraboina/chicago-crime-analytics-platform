"""
==========================================================
Monthly Crime Analysis
==========================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.plotly_theme import apply_plotly_theme


# ==========================================================
# Prepare Data
# ==========================================================

def prepare_monthly_data(filtered_df):

    month_order = [

        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",

    ]

    monthly_df = (

        filtered_df

        .groupby("MonthName")

        .size()

        .reindex(month_order, fill_value=0)

        .reset_index(name="Crime Count")

    )

    total = monthly_df["Crime Count"].sum()

    monthly_df["Percentage"] = (

        monthly_df["Crime Count"]

        / total

        * 100

    ).round(2)

    return monthly_df


# ==========================================================
# Monthly Trend Chart
# ==========================================================

def show_monthly_chart(filtered_df):

    monthly_df = prepare_monthly_data(filtered_df)

    st.subheader("📈 Monthly Crime Trend")

    fig = px.line(

        monthly_df,

        x="MonthName",

        y="Crime Count",

        markers=True,

    )

    fig.update_traces(

        line_color="#F59E0B",

        marker_color="#F59E0B",

        marker_size=8,

        line_width=3,

        hovertemplate=(

            "<b>%{x}</b><br>"

            "Crime Count : %{y:,}"

            "<extra></extra>"

        ),

    )

    fig.update_layout(

        title=None,

        xaxis_title=None,

        yaxis_title="Crime Count",

        showlegend=False,

    )

    fig = apply_plotly_theme(fig)

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


# ==========================================================
# Monthly Distribution Table
# ==========================================================

def show_monthly_table(filtered_df):

    monthly_df = prepare_monthly_data(filtered_df)

    st.subheader("📋 Monthly Crime Distribution")

    st.dataframe(

        monthly_df,

        hide_index=True,

        use_container_width=True,

        height=340,

    )


# ==========================================================
# Monthly Insights
# ==========================================================

def show_monthly_insights(filtered_df):

    monthly_df = prepare_monthly_data(filtered_df)

    highest = monthly_df.loc[
        monthly_df["Crime Count"].idxmax()
    ]

    lowest = monthly_df.loc[
        monthly_df["Crime Count"].idxmin()
    ]

    average = round(

        monthly_df["Crime Count"].mean(),

        1,

    )

    with st.container(border=True):

        st.subheader("📅 Monthly Insights")

        st.metric(

            "Peak Month",

            highest["MonthName"],

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

            f"Lowest : {lowest['MonthName']}"

        )

        st.divider()

        st.info(

            "Deploy additional resources during high-crime months."

        )