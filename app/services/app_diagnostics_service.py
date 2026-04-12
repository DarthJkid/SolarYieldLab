"""App-layer diagnostics service."""
from __future__ import annotations
import pandas as pd


def run_diagnostics(site_id: str) -> pd.DataFrame:
    """Run diagnostics pipeline for a site and return results."""
    raise NotImplementedError
