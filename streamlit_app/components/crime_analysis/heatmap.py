"""
==========================================================
Crime Hotspot Map
==========================================================
"""

import streamlit as st
import plotly.express as px


# ==========================================================
# Prepare Map Data
# ==========================================================

def prepare_heatmap_data(filtered_df):

    map_df = filtered_df.copy()

    map_df = map_df.dropna(

        subset=[

            "latitude",

            "longitude",

        ]

    )

    return map_df


# ==========================================================
# Hotspot Map
# ==========================================================

def show_heatmap(filtered_df):

    st.subheader("🗺️ Crime Hotspot Map")

    map_df = prepare_heatmap_data(filtered_df)

    if map_df.empty:

        st.warning(

            "No geographical data available."

        )

        return

    fig = px.scatter_map(

        map_df,

        lat="latitude",

        lon="longitude",

        color="primary_type",

        hover_name="primary_type",

        hover_data={

            "district_code": True,

            "community_code": True,

            "latitude": False,

            "longitude": False,

        },

        zoom=9,

        height=600,

    )

    fig.update_layout(

        map_style="carto-darkmatter",

        margin=dict(

            l=0,

            r=0,

            t=0,

            b=0,

        ),

        legend=dict(

            orientation="h",

            yanchor="bottom",

            y=1.02,

            xanchor="center",

            x=0.5,

        ),

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )