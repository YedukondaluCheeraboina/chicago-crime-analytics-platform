"""
==========================================================
Project Information
==========================================================
"""

import streamlit as st

from utils.load_css import load_css
from utils.db_connection import load_crime_data

from components.layout.header import show_header
from components.layout.footer import show_footer

from components.ui.hero import show_hero
from components.ui.status import show_status
from components.ui.highlights import show_project_highlights
from components.ui.architecture import show_architecture
from components.ui.tech_stack import show_technology_stack
from components.ui.modules import show_modules
from components.ui.developer import show_developer


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="Project Information",

    page_icon="ℹ️",

    layout="wide",

)

load_css()

show_header(

    "Project Information",

    "Chicago Crime Analytics Platform",

)

crime_df = load_crime_data()


# ==========================================================
# Hero
# ==========================================================

show_hero()


# ==========================================================
# Executive Overview
# ==========================================================

show_status(crime_df)


st.divider()


# ==========================================================
# Highlights & Architecture
# ==========================================================

left, right = st.columns(2)

with left:

    show_project_highlights()

with right:

    show_architecture()


st.divider()


# ==========================================================
# Technology & Modules
# ==========================================================

left, right = st.columns(2)

with left:

    show_technology_stack()

with right:

    show_modules()


st.divider()


# ==========================================================
# Developer
# ==========================================================

show_developer()


st.divider()


# ==========================================================
# Footer
# ==========================================================

show_footer()