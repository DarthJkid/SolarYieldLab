"""Nsrdb API client."""
from __future__ import annotations
from src.ingestion.clients.base_client import BaseClient


class NSRDBClient(BaseClient):
    """Nsrdb data source client."""

    def fetch(self, **kwargs) -> dict:
        """Fetch data from Nsrdb."""
        raise NotImplementedError
