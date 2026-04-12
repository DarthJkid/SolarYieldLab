"""Enumerations used throughout the project."""
from enum import Enum


class DataSource(str, Enum):
    NASA_POWER = "nasa_power"
    PVWATTS = "pvwatts"
    PVGIS = "pvgis"
    NSRDB = "nsrdb"
    ERA5 = "era5"
    CAMS = "cams"


class AppEnv(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class AnomalyLabel(str, Enum):
    NORMAL = "normal"
    ANOMALY = "anomaly"
    UNCERTAIN = "uncertain"
