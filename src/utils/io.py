"""I/O utility functions."""
import json
from pathlib import Path
import pandas as pd
import yaml

def read_json(path: Path) -> dict:
    """Read a JSON file and return its contents as a dictionary."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def write_json(data: dict, path: Path) -> None:
    """Write a dictionary to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

def read_yaml(path: Path) -> dict:
    """Read a YAML file and return its contents as a dictionary."""
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def write_csv(df: pd.DataFrame, path: Path) -> None:
    """Write a DataFrame to a CSV file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)

def read_csv(path: Path) -> pd.DataFrame:
    """Read a CSV file and return its contents as a DataFrame."""
    return pd.read_csv(path)