import streamlit as st
import plotly.express as px

from utils.plotly_theme import apply_plotly_theme


def show_trend_charts(filtered_df):

    left, right = st.columns(2)

    # -------------------------------
    # Crime Trend by Year
    # -------------------------------
    with left:

        st.subheader("📈 Crime Trend by Year")

        yearly = (
            filtered_df.groupby("Year")
            .size()
            .reset_index(name="Crime Count")
        )

        fig = px.line(
            yearly,
            x="Year",
            y="Crime Count",
            markers=True,
        )

        # Apply global layout theme structure first
        fig = apply_plotly_theme(fig)
        
        # Override chart titles explicitly to empty strings to avoid 'undefined'
        fig.update_layout(
            title="",
            xaxis_title="Year",
            yaxis_title="Crime Count"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -------------------------------
    # Crime Distribution
    # -------------------------------
    with right:

        st.subheader("🥧 Crime Distribution")

        crime_type = (
            filtered_df["primary_type"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        crime_type.columns = [
            "Crime Type",
            "Count",
        ]

        fig = px.pie(
            crime_type,
            names="Crime Type",
            values="Count",
            hole=.55,
        )

        fig = apply_plotly_theme(fig)
        
        fig.update_layout(
            title=""
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )