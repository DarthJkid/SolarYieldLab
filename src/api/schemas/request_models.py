"""Pydantic request models for the API."""
from pydantic import BaseModel


class SimulationRequest(BaseModel):
    site_id: str
    source: str = "nasa_power"
    tilt: float = 20.0
    azimuth: float = 180.0
    losses_pct: float = 14.0
