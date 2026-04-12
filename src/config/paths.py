"""Resolved filesystem paths for the project."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RAW = DATA / "raw"
INTERIM = DATA / "interim"
PROCESSED = DATA / "processed"
FEATURE_STORE = DATA / "feature_store"
ARTIFACTS = DATA / "artifacts"
REGISTRY = DATA / "registry"
CONFIGS = ROOT / "configs"
