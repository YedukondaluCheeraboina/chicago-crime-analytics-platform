import streamlit as st
from datetime import datetime


def show_hero():

    hour = datetime.now().hour

    if hour < 12:
        greeting = "🌅 Good Morning"
    elif hour < 17:
        greeting = "☀️ Good Afternoon"
    else:
        greeting = "🌙 Good Evening"

    st.markdown(f"### {greeting}")

    st.title("🚔 Chicago Crime Analytics")

    st.markdown(
        """
### Interactive Crime Intelligence & Decision Support Dashboard
"""
    )

    st.write(
        """
Monitor crime trends, analyze hotspot locations, generate business
reports and explore interactive visualizations built using Python,
MySQL, Pandas, Plotly and Streamlit.
"""
    )

    st.write("")

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "📊 Explore Dashboard",
            use_container_width=True,
            type="primary"
        ):
            st.switch_page("pages/1_Dashboard.py")

    with c2:

        if st.button(
            "📑 View Reports",
            use_container_width=True
        ):
            st.switch_page("pages/4_MySQL_Reports.py")

    st.write("")

    st.markdown(
        """
### 🟢 LIVE SYSTEM STATUS
"""
    )

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.success("🗄 DB Connected")

    with s2:
        st.success("⚙ ETL Completed")

    with s3:
        st.success("📈 Dashboard Online")

    with s4:
        st.success("🕒 Updated Just Now")

    st.divider()