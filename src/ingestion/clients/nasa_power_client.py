"""Nasa Power API client."""
from __future__ import annotations
from src.ingestion.clients.base_client import BaseClient


class NASAPowerClient(BaseClient):
    """Nasa Power data source client."""

    def fetch(self, **kwargs) -> dict:
        """Fetch data from Nasa Power."""
        raise NotImplementedError
