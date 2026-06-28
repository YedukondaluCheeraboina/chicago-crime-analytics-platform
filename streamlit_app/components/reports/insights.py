"""
==========================================================
MySQL Reports Insights
==========================================================
"""

import streamlit as st


# ==========================================================
# Insight Card
# ==========================================================

def _insight_card(
    title: str,
    metric1_label: str,
    metric1_value,
    metric2_label: str,
    metric2_value,
    recommendation: str,
    card_type: str = "info",
):

    with st.container(border=True):

        st.subheader(title)

        st.metric(

            metric1_label,

            metric1_value,

        )

        st.metric(

            metric2_label,

            metric2_value,

        )

        st.divider()

        if card_type == "success":

            st.success(recommendation)

        elif card_type == "warning":

            st.warning(recommendation)

        else:

            st.info(recommendation)


# ==========================================================
# Database Insights
# ==========================================================

def show_reports_insights(
    yearly_df,
    category_df,
):

    st.subheader("💡 Database Insights")

    highest_year = yearly_df.loc[
        yearly_df["Crime_Count"].idxmax()
    ]

    lowest_year = yearly_df.loc[
        yearly_df["Crime_Count"].idxmin()
    ]

    top_category = category_df.loc[
        category_df["Crime_Count"].idxmax()
    ]

    second_category = category_df.sort_values(
        "Crime_Count",
        ascending=False
    ).iloc[1]

    col1, col2 = st.columns(2)

    with col1:

        _insight_card(

            title="📅 Year Analysis",

            metric1_label="Highest Crime Year",

            metric1_value=int(
                highest_year["Year"]
            ),

            metric2_label="Crime Count",

            metric2_value=f"{highest_year['Crime_Count']:,}",

            recommendation=(
                f"Arrest Rate : "
                f"{highest_year['Arrest_Rate']:.2f}%"
            ),

            card_type="info",

        )

        st.caption(

            f"Lowest Crime Year : "
            f"{int(lowest_year['Year'])}"

        )

    with col2:

        _insight_card(

            title="🚔 Category Analysis",

            metric1_label="Top Category",

            metric1_value=top_category["Primary_Type"],

            metric2_label="Crime Count",

            metric2_value=f"{top_category['Crime_Count']:,}",

            recommendation=(
                f"Contribution : "
                f"{top_category['Crime_Percentage']:.2f}%"
            ),

            card_type="success",

        )

        st.caption(

            "Second Highest : "

            f"{second_category['Primary_Type']}"

        )

    st.divider()