import streamlit as st


def render(html: str):
    try:
        # Streamlit 1.49+ supports HTML rendering directly
        st.html(html)
    except AttributeError:
        # Fallback for older versions
        st.markdown(html, unsafe_allow_html=True)