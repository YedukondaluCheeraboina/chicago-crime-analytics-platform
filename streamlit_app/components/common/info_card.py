"""
==========================================================
Reusable Information Card
==========================================================
Project : Chicago Crime Analytics
Description :
Reusable insight card for Dashboard, Crime Analysis,
Statistical Analysis and Reports.
==========================================================
"""

import streamlit as st


# ==========================================================
# Reusable Information Card
# ==========================================================

def info_card(
    title: str,
    items: list[str],
    icon: str = "📊",
    color: str = "#3B82F6",
):
    """
    Display a reusable information card.
    """

    html = f"""
    <div style="
        background:#1F2937;
        border:1px solid #374151;
        border-left:6px solid {color};
        border-radius:14px;
        padding:20px;
        min-height:360px;
        box-sizing:border-box;
        box-shadow:0px 4px 12px rgba(0,0,0,.25);
        display:flex;
        flex-direction:column;
    ">

        <div style="
            display:flex;
            align-items:center;
            gap:10px;
            margin-bottom:18px;
        ">

            <span style="
                font-size:24px;
            ">
                {icon}
            </span>

            <span style="
                font-size:18px;
                font-weight:700;
                color:#F8FAFC;
            ">
                {title}
            </span>

        </div>
    """

    for item in items:

        if item.strip() == "":
            html += """
            <div style="height:12px;"></div>
            """
            continue

        html += f"""
        <div style="
            display:flex;
            align-items:flex-start;
            gap:10px;
            margin-bottom:12px;
        ">

            <span style="
                color:{color};
                font-size:18px;
                font-weight:bold;
                line-height:1.4;
            ">
                •
            </span>

            <span style="
                color:#D1D5DB;
                font-size:14px;
                line-height:1.7;
            ">
                {item}
            </span>

        </div>
        """

    html += """
    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True,
    )