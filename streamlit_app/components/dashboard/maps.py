"""
==========================================================
Interactive Crime Map
==========================================================
"""

import streamlit as st
import plotly.express as px


def show_crime_map(filtered_df):

    st.subheader("🗺️ Interactive Crime Hotspot Map")

    # ----------------------------------------
    # Remove missing coordinates
    # ----------------------------------------

    map_df = filtered_df.dropna(
        subset=["latitude", "longitude"]
    )

    if map_df.empty:

        st.warning(
            "No geographical data available."
        )

        return

    # ----------------------------------------
    # Limit markers for better performance
    # ----------------------------------------

    if len(map_df) > 1000:

        map_df = map_df.sample(
            1000,
            random_state=42
        )

    # ----------------------------------------
    # Plotly Map
    # ----------------------------------------

    fig = px.scatter_mapbox(

        map_df,

        lat="latitude",

        lon="longitude",

        color="primary_type",

        hover_name="primary_type",

        hover_data={
            "description": True,
            "community_code": True,
            "district_code": True,
            "latitude": False,
            "longitude": False
        },

        zoom=10,

        height=650

    )

    fig.update_layout(

        mapbox_style="carto-positron",

        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),

        legend_title="Crime Type"

    )

    st.plotly_chart(
        fig,
        width="stretch"
    )