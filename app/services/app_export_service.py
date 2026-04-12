"""App-layer export service."""
import pandas as pd
import io


def to_csv_bytes(df: pd.DataFrame) -> bytes:
    """Convert DataFrame to CSV bytes for download."""
    buffer = io.BytesIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue()
