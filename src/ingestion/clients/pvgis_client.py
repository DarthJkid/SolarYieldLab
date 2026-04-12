"""Pvgis API client."""
from __future__ import annotations
from src.ingestion.clients.base_client import BaseClient


class PVGISClient(BaseClient):
    """Pvgis data source client."""

    def fetch(self, **kwargs) -> dict:
        """Fetch data from Pvgis."""
        raise NotImplementedError
