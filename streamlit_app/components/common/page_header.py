"""
==========================================================
Reusable Page Header
==========================================================
"""

import streamlit as st


def show_page_header(
    title: str,
    subtitle: str = "",
    icon: str = "📊"
):

    st.markdown(
        f"""
<div style="
padding:10px 0 20px 0;
">

<h1 style="
color:#F9FAFB;
margin-bottom:8px;
">
{icon} {title}
</h1>

<p style="
font-size:18px;
color:#9CA3AF;
margin-top:0;
">
{subtitle}
</p>

</div>
""",
        unsafe_allow_html=True
    )