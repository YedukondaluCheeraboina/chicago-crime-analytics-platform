"""
==========================================================
Reusable Information Card
==========================================================
Project : Chicago Crime Analytics
Description : Safe card container that avoids HTML string leaks.
==========================================================
"""

import streamlit as st


def info_card(
    title: str,
    items: list[str],
    icon: str = "📊",
    color: str = "#3B82F6",
):
    """
    Display a reusable information card using clean container containment.
    """
    # Create the outer container layout block with custom CSS
    st.markdown(
        f"""
        <div style="
            background: #1F2937;
            border-left: 6px solid {color};
            border-radius: 16px;
            padding: 22px;
            margin-bottom: 15px;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.30);
        ">
            <h3 style="margin-top: 0; margin-bottom: 15px; color: white; font-weight: 700;">
                {icon} {title}
            </h3>
        """,
        unsafe_allow_html=True
    )

    # Render each row item cleanly
    for item in items:
        if not item or item.strip() == "":
            st.markdown("<div style='margin-bottom: 8px;'></div>", unsafe_allow_html=True)
        else:
            st.markdown(
                f"""
                <div style="color: #D1D5DB; font-size: 15px; margin-bottom: 10px; line-height: 1.5; padding-left: 5px;">
                    • {item}
                </div>
                """,
                unsafe_allow_html=True
            )

    # Close the outer wrapper container div safely
    st.markdown("</div>", unsafe_allow_html=True)