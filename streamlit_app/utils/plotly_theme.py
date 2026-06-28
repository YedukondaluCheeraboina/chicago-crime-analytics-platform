from plotly.graph_objects import Figure

# Color Palette Variables
BACKGROUND = "#0F172A"
PLOT_BACKGROUND = "#111827"
TEXT = "#F8FAFC"
SECONDARY_TEXT = "#CBD5E1"
GRID = "#334155"

def apply_plotly_theme(fig: Figure) -> Figure:
    """Applies a consistent dark theme across all charts without rendering 'undefined'."""
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font=dict(
            family="Segoe UI",
            size=14,
            color=TEXT,
        ),
        
        # Safe empty title initialization avoids JS frontend serialization bugs
        title="", 
        
        hovermode="closest",
        hoverlabel=dict(
            bgcolor="#1E293B",
            font=dict(color="white", size=13),
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(0,0,0,0)",
            font=dict(color=TEXT, size=12),
        ),
        margin=dict(l=15, r=15, t=20, b=15),
        autosize=True,
        height=420,
    )

    fig.update_xaxes(
        showgrid=False,
        showline=True,
        linecolor=GRID,
        linewidth=1,
        tickfont=dict(color=SECONDARY_TEXT, size=12),
        automargin=True,
        zeroline=False,
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID,
        gridwidth=1,
        showline=True,
        linecolor=GRID,
        linewidth=1,
        tickfont=dict(color=SECONDARY_TEXT, size=12),
        zeroline=False,
    )

    return fig