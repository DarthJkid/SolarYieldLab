"""Loader for site metadata CSV files."""
from __future__ import annotations
from pathlib import Path
import pandas as pd


def load_site_metadata(path: Path) -> pd.DataFrame:
    """Load and parse site metadata CSV."""
    return pd.read_csv(path)
