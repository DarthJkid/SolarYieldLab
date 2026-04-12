"""Diagnostic result model."""
from dataclasses import dataclass, field
import pandas as pd


@dataclass
class DiagnosticResult:
    """Output of the diagnostics pipeline for a site."""
    site_id: str
    anomaly_scores: pd.Series
    anomaly_labels: pd.Series
    residuals: pd.Series
    summary: dict = field(default_factory=dict)
