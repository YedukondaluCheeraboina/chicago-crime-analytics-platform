import streamlit as st
import plotly.express as px

from utils.plotly_theme import apply_plotly_theme


def show_hotspot_map(filtered_df):

    st.markdown("---")
    st.markdown("## 🗺️ Crime Hotspot Analysis")

    st.caption(
        "Interactive geographical visualization of crime incidents."
    )

    map_df = filtered_df[
        [
            "latitude",
            "longitude",
            "primary_type",
            "Year",
            "MonthName",
            "community_code"
        ]
    ].dropna(
        subset=["latitude", "longitude"]
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📍 Incidents",
            len(map_df)
        )

    with col2:
        st.metric(
            "🚔 Crime Categories",
            map_df["primary_type"].nunique()
        )

    with col3:
        st.metric(
            "🏘 Communities",
            map_df["community_code"].nunique()
        )

    if not map_df.empty:

        st.map(
            map_df,
            latitude="latitude",
            longitude="longitude",
            width='stretch',
        )

    else:

        st.warning(
            "No map data available for the selected filters."
        )

    st.markdown("")

    st.subheader("🏘️ Community Area Analysis")

    community_df = (
        filtered_df
        .groupby("community_code")
        .size()
        .reset_index(name="Crime_Count")
        .sort_values(
            by="Crime_Count",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        community_df,
        x="community_code",
        y="Crime_Count",
        color="Crime_Count",
        text="Crime_Count",
        # template="plotly_white",
        title="Top 10 Community Areas"
    )

    fig.update_traces(
        textposition="outside"
    )

    # fig.update_layout(
    # xaxis_title="Community Area",
    # yaxis_title="Crime Count"
    # )

    fig = apply_plotly_theme(fig)

    st.plotly_chart(
        fig,
        width='stretch'
    )

    if not community_df.empty:

        highest = community_df.iloc[0]
        lowest = community_df.iloc[-1]

        st.info(
            f"""
### 📍 Community Insights

**Highest Crime Area**

Community **{int(highest['community_code'])}**

({highest['Crime_Count']} crimes)

---

**Lowest Crime Area (Top 10)**

Community **{int(lowest['community_code'])}**

({lowest['Crime_Count']} crimes)
"""
        )