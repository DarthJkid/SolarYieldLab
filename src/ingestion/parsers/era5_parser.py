"""Era5 response parser."""
from __future__ import annotations
import pandas as pd


class ERA5Parser:
    """Era5 response parser."""

    def parse(self, raw: dict) -> pd.DataFrame:
        """Parse raw API response into a normalised DataFrame."""
        raise NotImplementedError
