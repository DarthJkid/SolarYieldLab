"""Hashing utilities."""
import hashlib
import json


def dict_hash(data: dict) -> str:
    """Return a stable SHA-256 hash of a dictionary."""
    serialised = json.dumps(data, sort_keys=True)
    return hashlib.sha256(serialised.encode()).hexdigest()
