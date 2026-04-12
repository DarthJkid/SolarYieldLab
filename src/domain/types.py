"""Custom type aliases used in the domain layer."""
from typing import NewType

SiteID = NewType("SiteID", str)
RunID = NewType("RunID", str)
Latitude = NewType("Latitude", float)
Longitude = NewType("Longitude", float)
