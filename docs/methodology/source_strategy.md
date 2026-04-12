# Data Source Strategy

## Primary Sources
- **NASA POWER**: Global coverage, free, hourly resolution
- **PVWatts**: NREL simulation API, validated against NSRDB

## Secondary Sources
- **PVGIS**: European focus, good coverage for EU sites
- **ERA5**: Reanalysis, best for historical periods

## Source Selection Logic
Sources are ranked by: spatial resolution → temporal coverage → uncertainty estimate.
