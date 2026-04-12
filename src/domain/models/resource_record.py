"""Solar resource record model."""
from dataclasses import dataclass
import pandas as pd


@dataclass
class ResourceRecord:
    """Harmonised solar resource record for a site and source."""
    site_id: str
    source: str
    data: pd.DataFrame
    units: dict
    metadata: dict
