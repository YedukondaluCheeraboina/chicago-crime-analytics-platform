import streamlit as st


def show_technology_stack():

    st.markdown("## 🛠 Technology Stack")

    col1, col2, col3 = st.columns(3)

    with col1:

        with st.container(border=True):

            st.subheader("Backend")

            st.write("🐍 Python")
            st.write("🗄 MySQL")
            st.write("⚙ SQLAlchemy")

    with col2:

        with st.container(border=True):

            st.subheader("Analytics")

            st.write("📊 Pandas")
            st.write("📈 Plotly")
            st.write("📉 NumPy")

    with col3:

        with st.container(border=True):

            st.subheader("Frontend")

            st.write("🌐 Streamlit")
            st.write("🎨 CSS")
            st.write("📱 Responsive UI")