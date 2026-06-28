import streamlit as st

from components.common.card import metric_card


def show_kpi_cards(metrics):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        metric_card(
            title="Total Crimes",
            value=f"{metrics['total_crimes']:,}",
            subtitle="Crime Records",
            icon="🚔",
            accent_color="#2563EB",
        )

    with col2:

        metric_card(
            title="Arrest Rate",
            value=f"{metrics['arrest_rate']:.1f}%",
            subtitle="Successful Arrests",
            icon="👮",
            accent_color="#10B981",
        )

    with col3:

        metric_card(
            title="Crime Types",
            value=metrics["crime_categories"],
            subtitle="Unique Categories",
            icon="📂",
            accent_color="#F59E0B",
        )

    with col4:

        metric_card(
            title="Districts",
            value=metrics["districts"],
            subtitle="Police Districts",
            icon="📍",
            accent_color="#8B5CF6",
        )