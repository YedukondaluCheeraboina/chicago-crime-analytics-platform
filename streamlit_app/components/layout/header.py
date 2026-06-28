"""
==========================================================
Reusable Page Header
==========================================================
"""

import streamlit as st


def show_header(title, subtitle):
    """
    Displays a professional page header.
    """

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(90deg,#0F172A,#1E3A8A);
            padding:25px;
            border-radius:15px;
            margin-bottom:25px;
            box-shadow:0px 5px 15px rgba(0,0,0,0.25);
        ">

        <h1 style="
            color:white;
            margin:0;
        ">
        🚔 {title}
        </h1>

        <p style="
            color:#DBEAFE;
            font-size:18px;
            margin-top:8px;
        ">
        {subtitle}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


