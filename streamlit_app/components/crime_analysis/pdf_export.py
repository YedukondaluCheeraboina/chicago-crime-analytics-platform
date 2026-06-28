"""
==========================================================
Crime Analysis PDF Export
==========================================================
"""

import io
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


# ==========================================================
# Helpers
# ==========================================================

styles = getSampleStyleSheet()


def heading(text):

    return Paragraph(f"<b>{text}</b>", styles["Heading2"])


def paragraph(text):

    return Paragraph(text, styles["BodyText"])


def space(height=12):

    return Spacer(1, height)


# ==========================================================
# PDF Generator
# ==========================================================

def create_crime_analysis_pdf(filtered_df):

    """
    Returns PDF bytes for download.
    """

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    story = []

    # ======================================================
    # Title
    # ======================================================

    story.append(
        Paragraph(
            "<b><font size=18>"
            "Chicago Crime Analytics"
            "</font></b>",
            styles["Title"],
        )
    )

    story.append(
        Paragraph(
            "<font size=13>"
            "Crime Analysis Report"
            "</font>",
            styles["Heading2"],
        )
    )

    story.append(space())

    story.append(

        paragraph(

            f"Generated on : "

            f"{datetime.now():%d %B %Y %I:%M %p}"

        )

    )

    story.append(space(20))

    # ======================================================
    # Executive Summary
    # ======================================================

    story.append(heading("Executive Summary"))

    total_crimes = len(filtered_df)

    total_categories = filtered_df["primary_type"].nunique()

    total_districts = filtered_df["district_code"].nunique()

    total_communities = filtered_df["community_code"].nunique()

    arrest_rate = (

        filtered_df["arrest"].mean()

        * 100

    )

    summary = [

        ["Metric", "Value"],

        ["Total Crimes", f"{total_crimes:,}"],

        ["Crime Categories", total_categories],

        ["Districts", total_districts],

        ["Communities", total_communities],

        ["Arrest Rate", f"{arrest_rate:.2f}%"],

    ]

    table = Table(summary)

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.grey),

                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),

            ]

        )

    )

    story.append(table)

    story.append(space(20))

    # ======================================================
    # Top Crime Categories
    # ======================================================

    story.append(

        heading(

            "Top Crime Categories"

        )

    )

    category = (

        filtered_df["primary_type"]

        .value_counts()

        .head(10)

        .reset_index()

    )

    category.columns = [

        "Crime Type",

        "Crime Count",

    ]

    data = [["Crime Type", "Count"]]

    for _, row in category.iterrows():

        data.append(

            [

                row["Crime Type"],

                int(row["Crime Count"]),

            ]

        )

    table = Table(data)

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.grey),

                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ]

        )

    )

    story.append(table)

    story.append(space(20))

    # ======================================================
    # Top Districts
    # ======================================================

    story.append(

        heading(

            "Top Districts"

        )

    )

    district = (

        filtered_df["district_code"]

        .value_counts()

        .head(10)

        .reset_index()

    )

    district.columns = [

        "District",

        "Crime Count",

    ]

    data = [["District", "Count"]]

    for _, row in district.iterrows():

        data.append(

            [

                row["District"],

                int(row["Crime Count"]),

            ]

        )

    table = Table(data)

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkgreen),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.grey),

                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ]

        )

    )

    story.append(table)

    story.append(space(20))

    # ======================================================
    # Recommendations
    # ======================================================

    story.append(

        heading(

            "Recommendations"

        )

    )

    story.append(

        paragraph(

            "• Increase police patrols in high-crime districts."

        )

    )

    story.append(

        paragraph(

            "• Deploy additional surveillance in hotspot communities."

        )

    )

    story.append(

        paragraph(

            "• Strengthen preventive policing for high-frequency crime categories."

        )

    )

    story.append(

        paragraph(

            "• Continue monthly crime trend monitoring."

        )

    )

    story.append(space(25))

    # ======================================================
    # Footer
    # ======================================================

    story.append(

        paragraph(

            "<b>Generated using Chicago Crime Analytics Platform</b>"

        )

    )

    story.append(

        paragraph(

            "Version 1.0"

        )

    )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf