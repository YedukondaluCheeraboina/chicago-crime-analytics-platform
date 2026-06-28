"""
==========================================================
Executive Insights Component
==========================================================
"""

import streamlit as st


def show_executive_insights(
    filtered_df,
    top_crime,
    arrest_rate
):

    st.markdown("## 🧠 Executive Insights")

    total = len(filtered_df)

    if total == 0:
        st.warning("No insights available.")
        return

    # Most affected community
    top_community = (
        filtered_df["community_code"]
        .value_counts()
        .idxmax()
    )

    # Peak hour
    peak_hour = (
        filtered_df["Hour"]
        .value_counts()
        .idxmax()
    )

    # Peak day
    peak_day = (
        filtered_df["DayOfWeek"]
        .value_counts()
        .idxmax()
    )

    crime_percent = (
        filtered_df["primary_type"]
        .value_counts(normalize=True)
        .max() * 100
    )

    st.info(
f"""
### 📊 Executive Summary

🚔 **{top_crime}** accounts for **{crime_percent:.1f}%** of crimes.

👮 Arrest Rate: **{arrest_rate:.2f}%**

🏘 Highest Crime Community: **{top_community}**

🕒 Peak Crime Hour: **{peak_hour}:00**

📅 Peak Crime Day: **{peak_day}**

### 💡 Recommendation

Increase patrols in Community **{top_community}**
during **{peak_hour}:00**,
especially for **{top_crime}** incidents.
"""
    )