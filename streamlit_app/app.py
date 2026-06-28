"""
==========================================================
Chicago Crime Analytics

Home Page
==========================================================
"""

import streamlit as st

from utils.load_css import load_css
from utils.db_connection import load_crime_data

from components.layout.footer import show_footer
from components.ui.status import show_status
from components.ui.modules import show_modules
from components.ui.tech_stack import show_technology_stack
from components.ui.highlights import show_project_highlights
from components.ui.architecture import show_architecture
from components.ui.developer import show_developer
from components.ui.hero import show_hero


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="Chicago Crime Analytics",

    page_icon="🚔",

    layout="wide"

)

# ==========================================================
# Load CSS
# ==========================================================

load_css()

# ==========================================================
# Load Dataset
# ==========================================================

crime_df = load_crime_data()

# ==========================================================
# Hero Banner
# ==========================================================

show_hero()

# st.markdown("---")

# ==========================================================
# System Status
# ==========================================================

show_status(crime_df)

st.markdown("---")

# ==========================================================
# Live Dataset Statistics
# ==========================================================

# show_status(crime_df)

# ==========================================================
# Application Modules
# ==========================================================

show_modules()

st.markdown("---")

# ==========================================================
# Technology Stack
# ==========================================================

show_technology_stack()

st.markdown("---")

# ==========================================================
# Project Highlights
# ==========================================================

show_project_highlights()

st.markdown("---")

# ==========================================================
# Architecture
# ==========================================================

show_architecture()

st.markdown("---")

# ==========================================================
# Developer
# ==========================================================

show_developer()

# ==========================================================
# Footer
# ==========================================================

show_footer()