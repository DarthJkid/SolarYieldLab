"""Shared plotting helpers."""
import plotly.graph_objects as go


def empty_figure(title: str = "") -> go.Figure:
    """Return an empty Plotly figure."""
    fig = go.Figure()
    fig.update_layout(title=title)
    return fig
