"""
==========================================================
Statistic Card
==========================================================
"""

import streamlit as st


def show_stat_card(title, value):

    st.markdown(
        f"""
<div style="
background:#111827;
padding:15px;
border-radius:12px;
text-align:center;
border:1px solid #374151;
">

<div style="
color:#9CA3AF;
font-size:14px;
">
{title}
</div>

<div style="
font-size:28px;
font-weight:bold;
color:white;
margin-top:8px;
">
{value}
</div>

</div>
""",
        unsafe_allow_html=True
    )