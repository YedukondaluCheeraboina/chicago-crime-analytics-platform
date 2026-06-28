"""
==========================================================
MySQL Reports Export Center
==========================================================
"""

import io
import pandas as pd
import streamlit as st

from components.reports.pdf_export import (
    create_mysql_report_pdf,
)


# ==========================================================
# CSV
# ==========================================================

def _csv_bytes(df):

    return df.to_csv(
        index=False
    ).encode("utf-8")


# ==========================================================
# Excel
# ==========================================================

def _excel_bytes(df):

    output = io.BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl",
    ) as writer:

        df.to_excel(
            writer,
            sheet_name="MySQL Report",
            index=False,
        )

    return output.getvalue()


# ==========================================================
# Export Center
# ==========================================================

def show_export_center(

    yearly_df,

    category_df,

    arrest_df,

    community_df,

    report_df,

    report_name,

):

    st.subheader("📤 Export Center")

    st.caption(
        "Download the selected MySQL report in multiple formats."
    )

    csv_data = _csv_bytes(report_df)

    excel_data = _excel_bytes(report_df)

    pdf_data = create_mysql_report_pdf(

        yearly_df,

        category_df,

        arrest_df,

        community_df,

    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.download_button(

            label="📄 Download CSV",

            data=csv_data,

            file_name=f"{report_name}.csv",

            mime="text/csv",

            use_container_width=True,

        )

    with col2:

        st.download_button(

            label="📗 Download Excel",

            data=excel_data,

            file_name=f"{report_name}.xlsx",

            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

            use_container_width=True,

        )

    with col3:

        st.download_button(

            label="📕 Download PDF",

            data=pdf_data,

            file_name="mysql_reports.pdf",

            mime="application/pdf",

            use_container_width=True,

        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.info(

            f"Current Report : **{report_name.replace('_', ' ').title()}**"

        )

    with right:

        st.success(

            "✅ Export files generated successfully."

        )