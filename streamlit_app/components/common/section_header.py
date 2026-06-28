"""
==========================================================
Reusable Section Header
==========================================================
"""

import streamlit as st


def show_section_header(
    title: str,
    icon: str = "📈"
):

    st.markdown(
        f"""
<h3 style="
color:#F9FAFB;
margin-top:30px;
margin-bottom:15px;
">
{icon} {title}
</h3>
""",
        unsafe_allow_html=True
    )