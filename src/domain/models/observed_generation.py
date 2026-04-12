"""Observed generation data model."""
from dataclasses import dataclass
import pandas as pd


@dataclass
class ObservedGeneration:
    """Observed generation time series for a site."""
    site_id: str
    data: pd.DataFrame
    timezone: str = "UTC"
