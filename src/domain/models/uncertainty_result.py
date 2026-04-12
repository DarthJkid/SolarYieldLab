"""Uncertainty quantification result model."""
from dataclasses import dataclass
import numpy as np


@dataclass
class UncertaintyResult:
    """Output of Monte Carlo uncertainty quantification."""
    site_id: str
    samples: np.ndarray
    p10: float
    p50: float
    p90: float
    std: float
