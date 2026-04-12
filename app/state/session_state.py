"""Streamlit session state management."""
import streamlit as st
from app.state.defaults import DEFAULT_STATE


def initialise_session_state() -> None:
    """Initialise session state with defaults if not already set."""
    for key, value in DEFAULT_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = value
