import streamlit as st


def show_project_highlights():

    st.markdown("## 🏆 Project Highlights")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.write("✅ ETL Pipeline")
            st.write("✅ Data Cleaning")
            st.write("✅ Feature Engineering")
            st.write("✅ Interactive Dashboard")
            st.write("✅ Crime Analysis")

    with col2:

        with st.container(border=True):

            st.write("✅ Statistical Analysis")
            st.write("✅ SQL Reporting")
            st.write("✅ Crime Hotspot Map")
            st.write("✅ Executive Insights")
            st.write("✅ CSV Export")