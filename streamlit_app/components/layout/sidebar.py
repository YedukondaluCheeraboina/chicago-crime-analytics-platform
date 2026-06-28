"""
==========================================================
Dashboard Sidebar
==========================================================
"""

import streamlit as st


def show_sidebar(crime_df):

    with st.sidebar:

        st.markdown("# 🎛 Dashboard Filters")

        st.caption(
            "Filter crime records to analyze trends."
        )

        st.divider()

        # -------------------------------
        # Year
        # -------------------------------

        years = ["All"] + sorted(
            crime_df["Year"].unique().tolist()
        )

        selected_year = st.selectbox(
            "📅 Select Year",
            years,
        )

        # -------------------------------
        # Crime Type
        # -------------------------------

        crime_types = ["All"] + sorted(
            crime_df["primary_type"].unique().tolist()
        )

        selected_crime = st.selectbox(
            "🚔 Crime Category",
            crime_types,
        )

        # -------------------------------
        # Top N
        # -------------------------------

        top_n = st.slider(
            "📊 Top Categories",
            min_value=5,
            max_value=20,
            value=10,
        )

        # -------------------------------
        # Sort Order
        # -------------------------------

        sort_order = st.radio(
            "↕ Sort Order",
            [
                "Descending",
                "Ascending"
            ],
            horizontal=True,
        )

        st.divider()

        st.markdown("### 📋 Active Filters")

        st.markdown(
            f"""
**Year**

{selected_year}

**Crime Type**

{selected_crime}

**Top Categories**

{top_n}

**Order**

{sort_order}
"""
        )

        st.divider()

        st.success("🟢 Dashboard Ready")

        return (
            selected_year,
            selected_crime,
            top_n,
            sort_order,
        )