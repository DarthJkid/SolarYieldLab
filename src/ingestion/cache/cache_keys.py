"""Functions for generating deterministic cache keys."""


def nasa_power_key(lat: float, lon: float, start: str, end: str) -> str:
    return f"nasa_power:{lat}:{lon}:{start}:{end}"


def pvwatts_key(lat: float, lon: float, capacity: float) -> str:
    return f"pvwatts:{lat}:{lon}:{capacity}"
