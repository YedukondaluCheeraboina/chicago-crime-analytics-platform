import streamlit as st

from utils.export_utils import (
    export_csv,
    export_excel,
    export_pdf,
    export_summary,
)


def show_download_center(filtered_df, metrics):

    st.markdown("---")

    st.header("📥 Export Center")

    csv = export_csv(filtered_df)

    excel = export_excel(filtered_df)

    pdf = export_pdf(metrics)

    summary = export_summary(metrics)

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.download_button(
            "📄 CSV",
            csv,
            "crime_data.csv",
            "text/csv",
            use_container_width=True,
        )

    with c2:

        st.download_button(
            "📊 Excel",
            excel,
            "crime_data.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )

    with c3:

        st.download_button(
            "📑 PDF",
            pdf,
            "crime_report.pdf",
            "application/pdf",
            use_container_width=True,
        )

    with c4:

        st.download_button(
            "📋 Summary",
            summary,
            "dashboard_summary.txt",
            "text/plain",
            use_container_width=True,
        )