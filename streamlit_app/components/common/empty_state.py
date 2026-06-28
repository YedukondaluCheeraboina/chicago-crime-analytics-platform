"""
==========================================================
Empty State
==========================================================
"""

import streamlit as st


def show_empty_state(message):

    st.markdown(
        f"""
<div style="
padding:40px;
text-align:center;
background:#1F2937;
border-radius:16px;
border:1px dashed #4B5563;
">

<h3>
📭 No Data Available
</h3>

<p>
{message}
</p>

</div>
""",
        unsafe_allow_html=True
    )