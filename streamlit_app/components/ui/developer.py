"""
==========================================================
Developer Information
==========================================================
"""

import streamlit as st


def show_developer():

    st.subheader("👨‍💻 Developer Information")

    left, right = st.columns([2, 1])

    # ======================================================
    # Left Section
    # ======================================================

    with left:

        with st.container(border=True):

            st.markdown("### 🚔 Chicago Crime Analytics Platform")

            st.write(
                """
An end-to-end Crime Intelligence & Decision Support System
developed using Python, Streamlit, MySQL, Pandas and Plotly.

The application provides interactive dashboards, crime analysis,
business intelligence reports, hotspot visualization, ETL
processing and statistical analysis to assist law enforcement
agencies in making data-driven decisions.
"""
            )

            st.divider()

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Language",
                    "Python"
                )

                st.metric(
                    "Database",
                    "MySQL"
                )

                st.metric(
                    "Frontend",
                    "Streamlit"
                )

            with c2:

                st.metric(
                    "Analytics",
                    "Pandas"
                )

                st.metric(
                    "Visualization",
                    "Plotly"
                )

                st.metric(
                    "Version",
                    "1.0"
                )

    # ======================================================
    # Right Section
    # ======================================================

    with right:

        with st.container(border=True):

            st.markdown("### 👤 Developer")

            st.success("Yedukondalu Cheeraboina")

            st.write("Software Developer")

            st.divider()

            st.metric(
                "Project Modules",
                "5"
            )

            st.metric(
                "Reusable Components",
                "40+"
            )

            st.metric(
                "Status",
                "Completed ✅"
            )

            st.divider()

            st.info(
                "Designed following modular architecture using reusable Streamlit components."
            )