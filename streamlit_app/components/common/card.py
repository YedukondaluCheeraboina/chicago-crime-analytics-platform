"""
==========================================================
Reusable Card Components
==========================================================
"""

import streamlit as st

# from components.common.theme import CARD_BG, BORDER, TEXT_PRIMARY, TEXT_SECONDARY


def metric_card(
    title: str,
    value,
    subtitle: str,
    icon: str,
    accent_color: str = "#3B82F6",
):
    """
    Display a reusable metric card.
    """

    st.markdown(
        f"""
<div style="
background:#1F2937;
border:1px solid #374151;
border-left:6px solid {accent_color};
border-radius:16px;
padding:18px;
height:160px;
box-shadow:0 6px 14px rgba(0,0,0,.35);
">

<div style="
font-size:15px;
font-weight:600;
color:#9CA3AF;
">
{icon} {title}
</div>

<div style="
font-size:34px;
font-weight:700;
margin-top:18px;
color:#F9FAFB;
">
{value}
</div>

<div style="
margin-top:14px;
font-size:13px;
color:#9CA3AF;
">
{subtitle}
</div>

</div>
""",
        unsafe_allow_html=True,
    )