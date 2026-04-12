"""File-based request cache to avoid redundant API calls."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path


class RequestCache:
    """Simple filesystem-based request cache."""

    def __init__(self, cache_dir: Path) -> None:
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _key_path(self, key: str) -> Path:
        hashed = hashlib.sha256(key.encode()).hexdigest()
        return self.cache_dir / f"{hashed}.json"

    def get(self, key: str) -> dict | None:
        path = self._key_path(key)
        if path.exists():
            return json.loads(path.read_text())
        return None

    def set(self, key: str, value: dict) -> None:
        self._key_path(key).write_text(json.dumps(value))
