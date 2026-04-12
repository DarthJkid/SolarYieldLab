"""Cams API client."""
from __future__ import annotations
from src.ingestion.clients.base_client import BaseClient


class CAMSClient(BaseClient):
    """Cams data source client."""

    def fetch(self, **kwargs) -> dict:
        """Fetch data from Cams."""
        raise NotImplementedError
