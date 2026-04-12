"""Default values for Streamlit session state."""
from typing import Any

DEFAULT_STATE: dict[str, Any] = {
    "selected_site_id": None,
    "simulation_results": None,
    "diagnostics_results": None,
    "active_sources": ["nasa_power", "pvwatts"],
}
