"""Utility decorators."""
import functools
import time
from src.utils.logging_utils import get_logger

logger = get_logger(__name__)


def retry(max_attempts: int = 3, delay: float = 1.0):
    """Retry decorator with fixed delay."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    logger.warning("Attempt %d/%d failed: %s", attempt + 1, max_attempts, exc)
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
                    else:
                        raise
        return wrapper
    return decorator
