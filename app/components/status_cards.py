"""Status card components."""
import streamlit as st


def metric_card(title: str, value: str, delta: str | None = None) -> None:
    """Render a metric card."""
    st.metric(label=title, value=value, delta=delta)
