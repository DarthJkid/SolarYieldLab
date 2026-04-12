"""Download button components."""
import streamlit as st
import pandas as pd
import io


def csv_download_button(df: pd.DataFrame, filename: str, label: str = "Download CSV") -> None:
    """Render a CSV download button for a DataFrame."""
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    st.download_button(label=label, data=buffer.getvalue(), file_name=filename, mime="text/csv")
