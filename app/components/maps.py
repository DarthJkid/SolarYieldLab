"""Map components using plotly."""
import plotly.express as px
import pandas as pd


def render_site_map(sites_df: pd.DataFrame) -> None:
    """Render a map of sites."""
    import streamlit as st
    fig = px.scatter_mapbox(
        sites_df, lat="lat", lon="lon", hover_name="name",
        zoom=3, height=450, mapbox_style="carto-positron",
    )
    st.plotly_chart(fig, use_container_width=True)
