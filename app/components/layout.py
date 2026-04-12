"""Shared layout utilities for Streamlit pages."""
import streamlit as st


def configure_page(title: str, icon: str = "☀️", layout: str = "wide") -> None:
    """Configure Streamlit page settings."""
    st.set_page_config(page_title=f"{title} | SolarYieldLab", page_icon=icon, layout=layout)
