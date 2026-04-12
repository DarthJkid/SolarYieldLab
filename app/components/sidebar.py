"""Sidebar component."""
import streamlit as st


def render_sidebar() -> None:
    """Render the global sidebar."""
    with st.sidebar:
        st.image("app/assets/logo.png", use_column_width=True)
        st.divider()
