"""
==========================================================
Crime Analysis Export Center
==========================================================
"""

import io
import pandas as pd
import streamlit as st

from components.crime_analysis.pdf_export import (
    create_crime_analysis_pdf,
)


# ==========================================================
# CSV Export
# ==========================================================

def _csv_bytes(df):

    return df.to_csv(
        index=False
    ).encode("utf-8")


# ==========================================================
# Excel Export
# ==========================================================

def _excel_bytes(df):

    output = io.BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl",
    ) as writer:

        df.to_excel(
            writer,
            sheet_name="Crime Analysis",
            index=False,
        )

    return output.getvalue()


# ==========================================================
# Export Center
# ==========================================================

def show_crime_export(filtered_df):

    st.subheader("📤 Export Center")

    st.caption(
        "Download the filtered crime analysis report in multiple formats."
    )

    csv_data = _csv_bytes(filtered_df)

    excel_data = _excel_bytes(filtered_df)

    pdf_data = create_crime_analysis_pdf(filtered_df)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.download_button(

            label="📄 Download CSV",

            data=csv_data,

            file_name="crime_analysis.csv",

            mime="text/csv",

            use_container_width=True,

        )

    with col2:

        st.download_button(

            label="📗 Download Excel",

            data=excel_data,

            file_name="crime_analysis.xlsx",

            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

            use_container_width=True,

        )

    with col3:

        st.download_button(

            label="📕 Download PDF",

            data=pdf_data,

            file_name="crime_analysis_report.pdf",

            mime="application/pdf",

            use_container_width=True,

        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.info(

            f"Records Available : **{len(filtered_df):,}**"

        )

    with right:

        st.success(

            "✅ Export files generated successfully."

        )