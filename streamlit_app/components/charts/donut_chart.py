"""
==========================================================
Reusable Plotly Donut Chart
==========================================================
Project : Chicago Crime Analytics
Description :
Reusable donut chart component for the entire application.
==========================================================
"""

import plotly.express as px

from utils.plotly_theme import apply_plotly_theme


# ==========================================================
# Reusable Donut Chart
# ==========================================================

def create_donut_chart(
    dataframe,
    names: str,
    values: str,
    title: str | None = None,
    hole: float = 0.60,
):
    """
    Create a reusable Plotly donut chart.

    Parameters
    ----------
    dataframe : pandas.DataFrame

    names : str
        Column containing category names.

    values : str
        Column containing values.

    title : str | None

    hole : float

    Returns
    -------
    plotly.graph_objects.Figure
    """

    fig = px.pie(

        dataframe,

        names=names,

        values=values,

        hole=hole,

    )

    # ======================================================
    # Styling
    # ======================================================

    fig.update_traces(

        textinfo="percent",

        textposition="inside",

        insidetextorientation="radial",

        hovertemplate=(
            "<b>%{label}</b><br>"
            "Count : %{value}<br>"
            "Percentage : %{percent}<extra></extra>"
        ),

        marker=dict(

            line=dict(

                color="#0F172A",

                width=2,

            )

        ),

    )

    # Slightly pull out the largest slice
    if len(dataframe) > 0:

        pull = [0.05] + [0] * (len(dataframe) - 1)

        fig.update_traces(pull=pull)

    # ======================================================
    # Layout
    # ======================================================

    fig.update_layout(

        title=None,

        showlegend=True,

        legend=dict(

            orientation="v",

            y=0.5,

            x=1.02,

            yanchor="middle",

            bgcolor="rgba(0,0,0,0)",

        ),

    )

    # ======================================================
    # Apply Global Theme
    # ======================================================

    fig = apply_plotly_theme(fig)

    return fig