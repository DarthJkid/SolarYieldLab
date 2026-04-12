"""Table display components."""
import pandas as pd
import streamlit as st


def render_site_table(sites_df: pd.DataFrame) -> None:
    """Render a formatted sites table."""
    st.dataframe(sites_df, use_container_width=True)
