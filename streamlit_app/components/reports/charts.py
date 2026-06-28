"""
==========================================================
MySQL Reports Charts
==========================================================
"""

import streamlit as st
import plotly.express as px

from utils.plotly_theme import apply_plotly_theme


# ==========================================================
# Yearly Crime Trend
# ==========================================================

def show_yearly_chart(yearly_df):

    st.subheader("📅 Yearly Crime Trend")

    fig = px.line(

        yearly_df,

        x="Year",

        y="Crime_Count",

        markers=True,

    )

    fig.update_traces(

        line_color="#2563EB",

        marker_color="#2563EB",

        marker_size=8,

        line_width=3,

        hovertemplate="<b>%{x}</b><br>Crime Count : %{y:,}<extra></extra>",

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
# Crime Categories
# ==========================================================

def show_category_chart(category_df):

    st.subheader("🚔 Crime Categories")

    fig = px.bar(

        category_df,

        x="Crime_Count",

        y="Primary_Type",

        orientation="h",

        color="Crime_Count",

        color_continuous_scale="Blues",

    )

    fig.update_layout(

        title=None,

        xaxis_title="Crime Count",

        yaxis_title=None,

        coloraxis_showscale=False,

    )

    fig = apply_plotly_theme(fig)

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


# ==========================================================
# Arrest Report
# ==========================================================

def show_arrest_chart(arrest_df):

    st.subheader("👮 Yearly Arrest Report")

    fig = px.bar(

        arrest_df,

        x="Year",

        y="Arrest_Count",

        text="Arrest_Count",

        color="Arrest_Count",

        color_continuous_scale="Greens",

    )

    fig.update_traces(

        textposition="outside",

    )

    fig.update_layout(

        title=None,

        xaxis_title=None,

        yaxis_title="Arrests",

        coloraxis_showscale=False,

    )

    fig = apply_plotly_theme(fig)

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


# ==========================================================
# Community Chart
# ==========================================================

def show_community_chart(community_df):

    st.subheader("🏘 Top Community Areas")

    community_df = community_df.head(10)

    fig = px.bar(

        community_df,

        x="community_code",

        y="Crime_Count",

        text="Crime_Count",

        color="Crime_Count",

        color_continuous_scale="Oranges",

    )

    fig.update_traces(

        textposition="outside",

    )

    fig.update_layout(

        title=None,

        xaxis_title="Community",

        yaxis_title="Crime Count",

        coloraxis_showscale=False,

    )

    fig = apply_plotly_theme(fig)

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


# ==========================================================
# Dashboard Layout
# ==========================================================

def show_reports_charts(

    yearly_df,

    category_df,

    arrest_df,

    community_df,

):

    col1, col2 = st.columns(2)

    with col1:

        show_yearly_chart(yearly_df)

    with col2:

        show_category_chart(category_df)

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        show_arrest_chart(arrest_df)

    with col4:

        show_community_chart(community_df)