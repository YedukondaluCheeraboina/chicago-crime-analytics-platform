import streamlit as st

def show_business_insights(metrics):
    st.markdown("---")
    st.header("💡 Executive Insights")

    col1, col2, col3 = st.columns([1.5, 1.5, 2])

    with col1:
        st.metric(
            label="🏆 Most Frequent Crime",
            value=metrics["top_crime"]
        )
        st.metric(
            label="📊 Crime Incidents",
            value=f"{metrics['top_crime_count']:,}"
        )

    with col2:
        st.metric(
            label="🚔 Arrest Rate",
            value=f"{metrics['arrest_rate']:.1f}%"
        )

    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if metrics["arrest_rate"] >= 40:
            st.success("✅ **Excellent Performance**\n\nCurrent clearance vectors align perfectly with target benchmarks.")
        elif metrics["arrest_rate"] >= 30:
            st.warning("⚠️ **Moderate Performance**\n\nArrest rates are stable, but monitoring protocols should remain active.")
        else:
            st.error("🚨 **Low Enforcement Performance**\n\nLow overall arrest yield discovered. Strategic tactical reallocations highly recommended.")