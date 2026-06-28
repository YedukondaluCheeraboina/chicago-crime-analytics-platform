"""
==========================================================
Crime Analysis Header
==========================================================
"""

from components.common.page_header import show_page_header


def show_crime_analysis_header():
    """
    Display the Crime Analysis page header.
    """

    show_page_header(
        title="Crime Analysis",
        subtitle=(
            "Explore crime categories, district-wise patterns, "
            "community trends and temporal analysis."
        ),
        icon="🚔",
    )