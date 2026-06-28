"""
==========================================================
Dashboard Header
==========================================================
"""

import streamlit as st
from datetime import datetime


def show_dashboard_header(metrics):

    current_time = datetime.now().strftime("%d %b %Y • %I:%M %p")

    st.markdown(
        """
# 🚔 Crime Analytics Dashboard
### Executive Business Intelligence & Decision Support System
"""
    )

    st.caption(
        "Analyze crime trends, monitor public safety, and generate actionable insights using interactive analytics."
    )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.info(f"📊 **Records**\n\n{metrics['total_crimes']:,}")

    with c2:
        st.success(f"📅 **Updated**\n\n{current_time}")

    with c3:
        st.success("🟢 **Status**\n\nOperational")

    with c4:
        st.info("🗄 **Source**\n\nMySQL Database")

    st.divider()