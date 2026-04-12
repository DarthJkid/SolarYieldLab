"""Simulation run model."""
from dataclasses import dataclass, field
from datetime import datetime
import pandas as pd
from src.domain.types import RunID, SiteID


@dataclass
class SimulationRun:
    """Results of a PV yield simulation run."""
    run_id: RunID
    site_id: SiteID
    source: str
    started_at: datetime
    completed_at: datetime | None = None
    results: pd.DataFrame | None = None
    metrics: dict = field(default_factory=dict)
