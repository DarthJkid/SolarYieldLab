# API Endpoints

## Health
- `GET /health` — service health check

## Sites
- `GET /sites` — list sites
- `POST /sites` — create site
- `GET /sites/{site_id}` — get site details

## Simulation
- `POST /simulation/run` — run PV simulation
- `GET /simulation/{run_id}` — get simulation results

## Diagnostics
- `POST /diagnostics/run` — run diagnostics pipeline
- `GET /diagnostics/{site_id}` — get diagnostics results
