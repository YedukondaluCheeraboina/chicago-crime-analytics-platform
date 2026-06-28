import streamlit as st
import plotly.express as px

from utils.plotly_theme import apply_plotly_theme


def show_analysis_charts(
    filtered_df,
    crime_df,
    selected_year,
    top_n,
    sort_order,
):

    st.markdown("---")

    left_col, right_col = st.columns(2)

    # ==========================================
    # Arrest Trend
    # ==========================================

    with left_col:

        if selected_year == "All":

            title = "👮 Arrest Trend (2015–2023)"

            arrest_summary = (
                crime_df.groupby("Year")["arrest"]
                .sum()
                .reset_index(name="Arrest_Count")
            )

            x_axis = "Year"

        else:

            title = f"👮 Monthly Arrest Trend ({selected_year})"

            arrest_summary = (
                filtered_df
                .groupby(["Month", "MonthName"])["arrest"]
                .sum()
                .reset_index(name="Arrest_Count")
                .sort_values("Month")
            )

            x_axis = "MonthName"

        st.subheader(title)

        fig = px.line(
            arrest_summary,
            x=x_axis,
            y="Arrest_Count",
            markers=True,
            title=title,
            # template="plotly_white",
        )

        # fig.update_layout(
        #     xaxis_title=x_axis,
        #     yaxis_title="Number of Arrests"
        # )

        fig = apply_plotly_theme(fig)

        st.plotly_chart(
            fig,
            width='stretch',
        )

    # ==========================================
    # Donut Chart
    # ==========================================

    with right_col:

        if selected_year == "All":
            title = f"🥧 Top {top_n} Crime Categories"
        else:
            title = f"🥧 Top {top_n} Crime Categories ({selected_year})"

        st.subheader(title)

        percentage_df = (
            filtered_df
            .groupby("primary_type")
            .size()
            .reset_index(name="Crime_Count")
        )

        percentage_df["Percentage"] = (
            percentage_df["Crime_Count"]
            / percentage_df["Crime_Count"].sum()
            * 100
        )

        ascending = sort_order == "Ascending"

        percentage_df = (
            percentage_df
            .sort_values(
                by="Crime_Count",
                ascending=ascending,
            )
            .head(top_n)
        )

        fig = px.pie(
            percentage_df,
            names="primary_type",
            values="Crime_Count",
            hole=0.55,
            title=title,
            # template="plotly_white",
        )

        fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
        )

        fig.update_layout(
            height=450,
        )

        st.plotly_chart(
            fig,
            width='stretch',
        )