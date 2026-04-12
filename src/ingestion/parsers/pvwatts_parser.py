"""Pvwatts response parser."""
from __future__ import annotations
import pandas as pd


class PVWattsParser:
    """Pvwatts response parser."""

    def parse(self, raw: dict) -> pd.DataFrame:
        """Parse raw API response into a normalised DataFrame."""
        raise NotImplementedError
