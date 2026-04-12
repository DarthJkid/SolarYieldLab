"""Nasa Power response parser."""
from __future__ import annotations
import pandas as pd


class NASAPowerParser:
    """Nasa Power response parser."""

    def parse(self, raw: dict) -> pd.DataFrame:
        """Parse raw API response into a normalised DataFrame."""
        raise NotImplementedError
