"""Loader for observed generation CSV files."""
from __future__ import annotations
from pathlib import Path
import pandas as pd


def load_observed_generation(path: Path) -> pd.DataFrame:
    """Load and parse observed generation CSV."""
    df = pd.read_csv(path, parse_dates=["timestamp"])
    return df
