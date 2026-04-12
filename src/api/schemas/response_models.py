"""Pydantic response models for the API."""
from pydantic import BaseModel


class SimulationResponse(BaseModel):
    run_id: str
    site_id: str
    status: str
    annual_yield_kwh: float | None = None
