import streamlit as st

from utils.load_css import load_css
from utils.db_connection import load_crime_data

from components.layout.header import show_header
from components.layout.sidebar import show_sidebar
from components.layout.footer import show_footer

from components.dashboard.header import show_dashboard_header
from components.dashboard.kpi_cards import show_kpi_cards
from components.dashboard.trend_charts import show_trend_charts
from components.dashboard.analysis_charts import show_analysis_charts
from components.dashboard.hotspot_map import show_hotspot_map
from components.dashboard.business_insights import show_business_insights
from utils.dashboard_metrics import calculate_dashboard_metrics
from components.dashboard.download_center import show_download_center


st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

load_css()

show_header(
    "Dashboard",
    "Interactive Business Intelligence Dashboard"
)

crime_df = load_crime_data()

(
    selected_year,
    selected_crime,
    top_n,
    sort_order
) = show_sidebar(crime_df)

filtered_df = crime_df.copy()

if selected_year != "All":
    filtered_df = filtered_df[
        filtered_df["Year"] == selected_year
    ]

if selected_crime != "All":
    filtered_df = filtered_df[
        filtered_df["primary_type"] == selected_crime
    ]

# ==========================================================
# Dashboard Metrics
# ==========================================================

metrics = calculate_dashboard_metrics(filtered_df)

# ==========================================================
# Dashboard Components
# ==========================================================

show_dashboard_header(metrics)
# After updating header.py later, this can become:
# show_dashboard_header(metrics)

show_kpi_cards(metrics)

show_trend_charts(filtered_df)

show_analysis_charts(
    filtered_df,
    crime_df,
    selected_year,
    top_n,
    sort_order
)

show_hotspot_map(filtered_df)

show_business_insights(metrics)

show_download_center(
    filtered_df,
    metrics
)

show_footer()