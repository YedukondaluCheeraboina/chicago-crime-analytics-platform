"""
==========================================================
Crime Analysis Recommendations
==========================================================
"""

import streamlit as st
from components.common.section_header import show_section_header

def show_recommendations(filtered_df):
    show_section_header(
        "Recommendations",
        "🎯"
    )

    if filtered_df.empty:
        return

    arrest_rate = (filtered_df["arrest"].mean() * 100)
    top_crime = filtered_df["primary_type"].value_counts().idxmax()

    recommendations = []

    if arrest_rate < 30:
        recommendations.append("Increase police patrols in high crime areas.")
    elif arrest_rate < 50:
        recommendations.append("Improve arrest efficiency through targeted operations.")
    else:
        recommendations.append("Maintain the current policing strategy.")

    if top_crime == "THEFT":
        recommendations.append("Increase surveillance in commercial zones.")
    elif top_crime == "BATTERY":
        recommendations.append("Deploy additional patrols during evening hours.")
    elif top_crime == "ASSAULT":
        recommendations.append("Focus on community policing initiatives.")
    else:
        recommendations.append("Monitor emerging crime trends regularly.")

    st.markdown("### Suggested Actions")
    
    # Generate flat inline layout strings to bypass code blocks entirely
    html_content = '<div style="background-color: #111827; border: 1px solid #1E293B; padding: 22px; border-radius: 12px;">'
    
    for index, recommendation in enumerate(recommendations, start=1):
        html_content += f'<div style="margin-bottom: 14px; padding: 12px; background-color: #1E293B; border-left: 4px solid #10B981; border-radius: 6px; color: #E2E8F0; font-size: 14px;"><b>{index}.</b> {recommendation}</div>'
        
    html_content += '</div>'
    st.markdown(html_content, unsafe_allow_html=True)
"""
==========================================================
Crime Analysis Recommendations
==========================================================
"""

import streamlit as st


# ==========================================================
# Generate Recommendations
# ==========================================================

def generate_recommendations(filtered_df):

    recommendations = []

    top_crime = (

        filtered_df["primary_type"]

        .value_counts()

        .idxmax()

    )

    top_district = (

        filtered_df["district_code"]

        .value_counts()

        .idxmax()

    )

    top_community = (

        filtered_df["community_code"]

        .value_counts()

        .idxmax()

    )

    arrest_rate = (

        filtered_df["arrest"]

        .mean()

        * 100

    )

    domestic_rate = (

        filtered_df["domestic"]

        .mean()

        * 100

    )

    recommendations.append(

        (
            "🚔 Patrol Deployment",
            f"Increase police patrols in District {top_district} where crime concentration is highest.",
            "High",
        )

    )

    recommendations.append(

        (
            "🏘 Community Safety",
            f"Strengthen surveillance and community policing in Community {top_community}.",
            "Medium",
        )

    )

    recommendations.append(

        (
            "⚠ Crime Prevention",
            f"Launch preventive campaigns targeting {top_crime} offences.",
            "Medium",
        )

    )

    if arrest_rate < 50:

        recommendations.append(

            (
                "👮 Arrest Efficiency",
                "Improve investigation and arrest efficiency through data-driven policing.",
                "High",
            )

        )

    if domestic_rate > 20:

        recommendations.append(

            (
                "🏠 Domestic Violence",
                "Increase awareness programs and victim support initiatives.",
                "Medium",
            )

        )

    recommendations.append(

        (
            "📊 Predictive Analytics",
            "Use historical crime trends to allocate officers proactively.",
            "Low",
        )

    )

    return recommendations


# ==========================================================
# Recommendation Card
# ==========================================================

def recommendation_card(

    title,

    description,

    priority,

):

    with st.container(border=True):

        left, right = st.columns([5, 1])

        with left:

            st.subheader(title)

            st.write(description)

        with right:

            if priority == "High":

                st.error(priority)

            elif priority == "Medium":

                st.warning(priority)

            else:

                st.success(priority)


# ==========================================================
# Dashboard Recommendations
# ==========================================================

def show_recommendations(filtered_df):

    st.subheader("🎯 Smart Recommendations")

    st.caption(

        "Recommendations generated from crime analytics."

    )

    recommendations = generate_recommendations(

        filtered_df

    )

    for title, description, priority in recommendations:

        recommendation_card(

            title,

            description,

            priority,

        )