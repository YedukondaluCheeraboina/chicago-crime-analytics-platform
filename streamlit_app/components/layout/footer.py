"""
==========================================================
Reusable Footer
==========================================================
"""

import streamlit as st
from datetime import datetime


def show_footer():

    st.markdown("---")

    st.markdown(
        f"""
        <div style="
            text-align:center;
            padding:20px;
            color:#64748B;
            font-size:15px;
        ">

        <b>🚔 Chicago Crime Analytics</b><br>

        Business Intelligence Platform<br><br>

        Built using
        <b>Python • MySQL • Streamlit • Plotly</b><br><br>

        Version 1.0<br>

        Generated on
        {datetime.now().strftime("%d %B %Y, %I:%M %p")}

        </div>
        """,
        unsafe_allow_html=True
    )