"""
==========================================================
MySQL Reports PDF Export
==========================================================
"""

import io
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


# ==========================================================
# Styles
# ==========================================================

styles = getSampleStyleSheet()


def heading(text):

    return Paragraph(

        f"<b>{text}</b>",

        styles["Heading2"],

    )


def paragraph(text):

    return Paragraph(

        text,

        styles["BodyText"],

    )


def space(height=12):

    return Spacer(

        1,

        height,

    )


# ==========================================================
# PDF Generator
# ==========================================================

def create_mysql_report_pdf(

    yearly_df,

    category_df,

    arrest_df,

    community_df,

):

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

            "MySQL Reports"

            "</font>",

            styles["Heading2"],

        )

    )

    story.append(space())

    story.append(

        paragraph(

            f"Generated On : "

            f"{datetime.now():%d %B %Y %I:%M %p}"

        )

    )

    story.append(space(20))

    # ======================================================
    # Executive Summary
    # ======================================================

    story.append(

        heading(

            "Executive Summary"

        )

    )

    total_years = yearly_df["Year"].nunique()

    total_categories = len(category_df)

    total_crimes = yearly_df["Crime_Count"].sum()

    avg_arrest = yearly_df["Arrest_Rate"].mean()

    summary = [

        ["Metric", "Value"],

        ["Years", total_years],

        ["Crime Categories", total_categories],

        ["Total Crimes", f"{int(total_crimes):,}"],

        ["Average Arrest Rate", f"{avg_arrest:.2f}%"],

    ]

    table = Table(summary)

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.grey),

                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

            ]

        )

    )

    story.append(table)

    story.append(space(20))

    # ======================================================
    # Yearly Report
    # ======================================================

    story.append(

        heading(

            "Yearly Crime Report"

        )

    )

    yearly = [["Year", "Crimes", "Arrests", "Rate"]]

    for _, row in yearly_df.iterrows():

        yearly.append(

            [

                int(row["Year"]),

                int(row["Crime_Count"]),

                int(row["Arrest_Count"]),

                f"{row['Arrest_Rate']:.2f}%",

            ]

        )

    table = Table(yearly)

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
    # Crime Categories
    # ======================================================

    story.append(

        heading(

            "Crime Category Report"

        )

    )

    category = [["Crime Type", "Count", "%"]]

    for _, row in category_df.head(10).iterrows():

        category.append(

            [

                row["Primary_Type"],

                int(row["Crime_Count"]),

                f"{row['Crime_Percentage']:.2f}%",

            ]

        )

    table = Table(category)

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
    # Arrest Report
    # ======================================================

    story.append(

        heading(

            "Yearly Arrest Report"

        )

    )

    arrests = [["Year", "Arrests"]]

    for _, row in arrest_df.iterrows():

        arrests.append(

            [

                int(row["Year"]),

                int(row["Arrest_Count"]),

            ]

        )

    table = Table(arrests)

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkred),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.grey),

                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ]

        )

    )

    story.append(table)

    story.append(space(20))

    # ======================================================
    # Community Summary
    # ======================================================

    story.append(

        heading(

            "Top Communities"

        )

    )

    community = [["Community", "Crime Count"]]

    for _, row in community_df.head(10).iterrows():

        community.append(

            [

                row["community_code"],

                int(row["Crime_Count"]),

            ]

        )

    table = Table(community)

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkorange),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.grey),

                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ]

        )

    )

    story.append(table)

    story.append(space(20))

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