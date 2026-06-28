"""
==========================================================
Reusable Plotly Bar Chart
==========================================================
Project : Chicago Crime Analytics
Description :
Reusable bar chart component for the entire application.
==========================================================
"""

import plotly.express as px

from utils.plotly_theme import apply_plotly_theme


# ==========================================================
# Reusable Bar Chart
# ==========================================================

def create_bar_chart(
    dataframe,
    x: str,
    y: str,
    title: str | None = None,
    color: str = "#3B82F6",
    orientation: str = "v",
    text: bool = True,
    sort: bool = False,
):
    """
    Create a reusable Plotly bar chart.

    Parameters
    ----------
    dataframe : DataFrame

    x : str

    y : str

    title : str

    color : str

    orientation : str

    text : bool

    sort : bool

    Returns
    -------
    Plotly Figure
    """

    # ======================================================
    # Sort Data
    # ======================================================

    if sort:

        dataframe = dataframe.sort_values(
            by=y,
            ascending=False,
        )

    # ======================================================
    # Create Chart
    # ======================================================

    fig = px.bar(

        dataframe,

        x=x if orientation == "v" else y,

        y=y if orientation == "v" else x,

        orientation=orientation,

        text=y if text else None,

    )

    # ======================================================
    # Trace Styling
    # ======================================================

    fig.update_traces(

        marker_color=color,

        marker_line_width=0,

        textposition="outside",

        hovertemplate=(
            "<b>%{x}</b><br>"
            "Count : %{y}<extra></extra>"
        ),

    )

    # ======================================================
    # Layout
    # ======================================================

    fig.update_layout(

        title=None,

        showlegend=False,

        coloraxis_showscale=False,

        xaxis_title=None,

        yaxis_title=None,

        bargap=0.25,

        uniformtext_minsize=10,

        uniformtext_mode="hide",

    )

    # ======================================================
    # Axis
    # ======================================================

    fig.update_xaxes(

        tickangle=-45,

        automargin=True,

    )

    fig.update_yaxes(

        rangemode="tozero",

    )

    # ======================================================
    # Apply Global Theme
    # ======================================================

    fig = apply_plotly_theme(fig)

    return fig