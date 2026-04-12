"""SolarYieldLab — Streamlit Home Page."""
import streamlit as st
from app.components.layout import configure_page
from app.state.session_state import initialise_session_state

configure_page(title="SolarYieldLab", icon="☀️")
initialise_session_state()

st.title("☀️ SolarYieldLab")
st.markdown(
    """
    **SolarYieldLab** is an integrated platform for solar yield simulation,
    diagnostics, and research.

    ### Navigation
    Use the sidebar to access:
    - 🗺️ **Site Explorer** — browse and manage solar sites
    - ⚙️ **System Designer** — configure PV system parameters
    - 📈 **Yield Simulator** — run multi-source simulations
    - 🔍 **Diagnostics** — anomaly detection and fault analysis
    - 🔬 **Research Dashboard** — cross-source comparison and uncertainty
    """
)
