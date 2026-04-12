"""Pvwatts API client."""
from __future__ import annotations
from src.ingestion.clients.base_client import BaseClient


class PVWattsClient(BaseClient):
    """Pvwatts data source client."""

    def fetch(self, **kwargs) -> dict:
        """Fetch data from Pvwatts."""
        raise NotImplementedError
