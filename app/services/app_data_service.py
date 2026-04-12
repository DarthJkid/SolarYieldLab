"""App-layer data service: loads and caches data for the UI."""
import pandas as pd
import streamlit as st


@st.cache_data(ttl=300)
def load_sites() -> pd.DataFrame:
    """Load sites from the processed store."""
    return pd.DataFrame(columns=["site_id", "name", "lat", "lon", "capacity_kw"])
