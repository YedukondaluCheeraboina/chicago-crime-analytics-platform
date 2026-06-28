import streamlit as st


def show_architecture():

    st.markdown("## 🏗 System Architecture")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.info("📂\n\nDataset")

    with col2:
        st.info("⚙️\n\nETL")

    with col3:
        st.info("🗄\n\nMySQL")

    with col4:
        st.info("📊\n\nAnalytics")

    with col5:
        st.info("🚔\n\nDashboard")

    st.markdown("---")

    st.markdown(
        """
**Workflow**

Dataset → Data Cleaning → Feature Engineering → MySQL → Interactive Dashboard
"""
    )