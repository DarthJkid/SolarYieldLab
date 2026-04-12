"""Shared pytest fixtures."""
import pytest
import pandas as pd
from pathlib import Path

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_sites_df() -> pd.DataFrame:
    return pd.read_csv(FIXTURES / "sample_sites.csv")


@pytest.fixture
def sample_observed_df() -> pd.DataFrame:
    return pd.read_csv(FIXTURES / "sample_observed_generation.csv", parse_dates=["timestamp"])


@pytest.fixture
def nasa_power_sample(tmp_path) -> dict:
    import json
    return json.loads((FIXTURES / "nasa_power_sample.json").read_text())
