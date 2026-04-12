"""PV system configuration model."""
from dataclasses import dataclass


@dataclass
class SystemConfig:
    """PV system configuration parameters."""
    capacity_kw: float
    tilt: float = 20.0
    azimuth: float = 180.0
    losses_pct: float = 14.0
    module_type: int = 1
    array_type: int = 1
