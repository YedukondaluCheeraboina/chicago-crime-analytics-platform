import streamlit as st


def show_modules():

    st.markdown("## 🚀 Application Modules")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("📊 Dashboard")

            st.write("• Executive KPIs")
            st.write("• Interactive Charts")
            st.write("• Crime Trends")
            st.write("• Performance Metrics")

        with st.container(border=True):

            st.subheader("📈 Statistical Analysis")

            st.write("• Distribution Analysis")
            st.write("• Pattern Discovery")
            st.write("• Correlation Analysis")
            st.write("• Visual Analytics")

    with col2:

        with st.container(border=True):

            st.subheader("🚔 Crime Analysis")

            st.write("• Crime Investigation")
            st.write("• Hotspot Mapping")
            st.write("• Executive Insights")
            st.write("• Crime Filtering")

        with st.container(border=True):

            st.subheader("🗄 MySQL Reports")

            st.write("• SQL Reports")
            st.write("• Summary Views")
            st.write("• Data Export")
            st.write("• Business Reports")