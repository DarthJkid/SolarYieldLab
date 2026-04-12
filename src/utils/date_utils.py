"""Date and time utilities."""
from datetime import datetime
import pandas as pd


def to_utc(dt: datetime) -> datetime:
    """Convert a datetime to UTC."""
    import pytz
    if dt.tzinfo is None:
        return pytz.utc.localize(dt)
    return dt.astimezone(pytz.utc)


def year_range(start: int, end: int) -> list[int]:
    """Return a list of years from start to end inclusive."""
    return list(range(start, end + 1))
