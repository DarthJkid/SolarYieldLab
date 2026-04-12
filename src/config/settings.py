"""Application settings loaded from environment variables."""
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()


@dataclass
class Settings:
    """Application settings loaded from environment variables."""
    app_name: str = os.getenv("APP_NAME", "SolarYieldLab")
    environment: str = os.getenv("ENVIRONMENT", "development")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    nasa_power_base_url: str = os.getenv
    (
        "NASA_POWER_BASE_URL",
        "https://power.larc.nasa.gov/api/temporal/hourly/point"
    )
    
    pvwatts_base_url: str = os.getenv(
        "PVWATTS_BASE_URL",
        "https://developer.nrel.gov/api/pvwatts/v8.json"
    )
    
    pvgis_base_url: str = os.getenv(
        "PVGIS_BASE_URL",
        "https://re.jrc.ec.europa.eu/api/v5_2/"
    )
    
    nrel_api_key: str = os.getenv("NREL_API_KEY", "")
    
    nsrdb_base_url: str = os.getenv(
        "NSRDB_BASE_URL",
        "https://developer.nrel.gov/api/nsrdb/v2/nsrdbapi.py"
    )
    
    


settings = Settings()
