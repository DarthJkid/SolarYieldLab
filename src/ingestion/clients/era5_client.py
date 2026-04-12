"""Era5 API client."""
from __future__ import annotations
from src.ingestion.clients.base_client import BaseClient


class ERA5Client(BaseClient):
    """Era5 data source client."""

    def fetch(self, **kwargs) -> dict:
        """Fetch data from Era5."""
        raise NotImplementedError
