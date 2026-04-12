"""Abstract base client for external data source APIs."""
from __future__ import annotations
from abc import ABC, abstractmethod
import requests
from src.utils.logging_utils import get_logger

logger = get_logger(__name__)


class BaseClient(ABC):
    """Abstract base class for all external API clients."""

    def __init__(self, base_url: str, timeout: int = 30, max_retries: int = 3) -> None:
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self._session = requests.Session()

    @abstractmethod
    def fetch(self, **kwargs) -> dict:
        """Fetch data from the API and return raw response."""
        ...

    def _get(self, url: str, params: dict | None = None) -> requests.Response:
        """Perform a GET request with retry logic."""
        for attempt in range(self.max_retries):
            try:
                response = self._session.get(url, params=params, timeout=self.timeout)
                response.raise_for_status()
                return response
            except requests.RequestException as exc:
                logger.warning("Request attempt %d/%d failed: %s", attempt + 1, self.max_retries, exc)
                if attempt == self.max_retries - 1:
                    raise
        raise RuntimeError("Unreachable")
