"""Application settings loaded from environment variables."""
from __future__ import annotations
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Central settings object."""
    NASA_POWER_BASE_URL: str = os.getenv("NASA_POWER_BASE_URL", "https://power.larc.nasa.gov/api/temporal")
    PVWATTS_API_KEY: str = os.getenv("PVWATTS_API_KEY", "")
    NSRDB_API_KEY: str = os.getenv("NSRDB_API_KEY", "")
    ERA5_API_KEY: str = os.getenv("ERA5_API_KEY", "")
    CAMS_API_KEY: str = os.getenv("CAMS_API_KEY", "")
    MLFLOW_TRACKING_URI: str = os.getenv("MLFLOW_TRACKING_URI", "./mlruns")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
