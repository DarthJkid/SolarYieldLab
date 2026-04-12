"""App-layer simulation service."""
from __future__ import annotations
import pandas as pd


def run_simulation(site_id: str, system_config: dict) -> pd.DataFrame:
    """Run a PV simulation for a site and return results."""
    raise NotImplementedError
