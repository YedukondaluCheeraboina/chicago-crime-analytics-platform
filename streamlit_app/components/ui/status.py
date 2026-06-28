import streamlit as st


def show_status(crime_df):
    st.markdown("## 📌 Executive Overview")

    total_records = len(crime_df)
    total_categories = crime_df["primary_type"].nunique()
    total_years = crime_df["Year"].nunique()

    arrest_rate = (
        crime_df["arrest"].sum() / total_records * 100
        if total_records > 0
        else 0
    )

    row1 = st.columns(4)

    with row1[0]:
        st.metric(
            "🟢 Database",
            "Connected"
        )

    with row1[1]:
        st.metric(
            "📊 Crime Records",
            f"{total_records:,}"
        )

    with row1[2]:
        st.metric(
            "🏷 Crime Categories",
            total_categories
        )

    with row1[3]:
        st.metric(
            "📅 Years",
            total_years
        )

    row2 = st.columns(4)

    with row2[0]:
        st.metric(
            "⚙ ETL",
            "Completed"
        )

    with row2[1]:
        st.metric(
            "🚔 Arrest Rate",
            f"{arrest_rate:.1f}%"
        )

    with row2[2]:
        st.metric(
            "🗂 Reports",
            "Ready"
        )

    with row2[3]:
        st.metric(
            "📈 Dashboard",
            "Online"
        )