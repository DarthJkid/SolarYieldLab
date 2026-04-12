"""Site domain model."""
from dataclasses import dataclass, field
from src.domain.types import SiteID, Latitude, Longitude


@dataclass
class Site:
    """Represents a solar generation site."""
    site_id: SiteID
    name: str
    lat: Latitude
    lon: Longitude
    capacity_kw: float
    tilt: float = 20.0
    azimuth: float = 180.0
    metadata: dict = field(default_factory=dict)
