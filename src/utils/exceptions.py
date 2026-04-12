"""Custom exceptions for SolarYieldLab."""


class SolarYieldLabError(Exception):
    """Base exception."""


class DataSourceError(SolarYieldLabError):
    """Raised when a data source request fails."""


class ValidationError(SolarYieldLabError):
    """Raised when data fails validation."""


class SimulationError(SolarYieldLabError):
    """Raised when a simulation fails."""


class ModelNotFoundError(SolarYieldLabError):
    """Raised when a requested model cannot be found in the registry."""
