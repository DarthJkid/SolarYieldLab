"""FastAPI dependency injection."""
from src.config.settings import settings


def get_settings():
    return settings
