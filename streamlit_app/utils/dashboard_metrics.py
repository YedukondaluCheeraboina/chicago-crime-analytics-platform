"""
==========================================================
Dashboard Metrics Utility
==========================================================
Calculates all dashboard KPIs and business metrics from
the filtered crime dataset.
==========================================================
"""


def calculate_dashboard_metrics(filtered_df):
    """
    Calculate dashboard metrics.

    Parameters
    ----------
    filtered_df : pandas.DataFrame

    Returns
    -------
    dict
    """

    total_crimes = len(filtered_df)

    total_arrests = filtered_df["arrest"].sum()

    arrest_rate = (
        total_arrests / total_crimes * 100
        if total_crimes > 0
        else 0
    )

    crime_categories = (
        filtered_df["primary_type"].nunique()
        if total_crimes > 0
        else 0
    )

    districts = (
        filtered_df["district_code"].nunique()
        if total_crimes > 0
        else 0
    )

    if total_crimes > 0:

        crime_counts = (
            filtered_df["primary_type"]
            .value_counts()
        )

        top_crime = crime_counts.idxmax()

        top_crime_count = crime_counts.max()

    else:

        top_crime = "N/A"

        top_crime_count = 0

    metrics = {

        "total_crimes": total_crimes,

        "total_arrests": total_arrests,

        "arrest_rate": arrest_rate,

        "crime_categories": crime_categories,

        "districts": districts,

        "top_crime": top_crime,

        "top_crime_count": top_crime_count

    }

    return metrics