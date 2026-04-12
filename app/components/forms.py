"""Reusable form components."""
import streamlit as st
from typing import Any


def site_input_form() -> dict[str, Any]:
    """Render a site input form and return user inputs."""
    with st.form("site_form"):
        name = st.text_input("Site Name")
        lat = st.number_input("Latitude", min_value=-90.0, max_value=90.0)
        lon = st.number_input("Longitude", min_value=-180.0, max_value=180.0)
        capacity = st.number_input("Capacity (kWp)", min_value=0.1)
        submitted = st.form_submit_button("Submit")
    return {"name": name, "lat": lat, "lon": lon, "capacity_kw": capacity, "submitted": submitted}
