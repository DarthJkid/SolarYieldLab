"""SolarYieldLab — Streamlit Home Page."""
import streamlit as st

st.set_page_config(
    page_title="SolarYieldLab",
    page_icon="☀️",
    layout="wide",
)

st.title("SolarYieldLab")
st.write(
    """
    SolarYieldLab is a research-grade solar resource, PV simulation,
    diagnostics, and analytics platform.

    This is the initial project shell. Core data ingestion and simulation
    modules will be connected next.
    """
)
