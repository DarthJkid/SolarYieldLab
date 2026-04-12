"""FastAPI application entry point."""
from fastapi import FastAPI
from src.api.routes import health, sites, simulation, diagnostics, metrics, exports

app = FastAPI(title="SolarYieldLab API", version="0.1.0", docs_url="/docs")

app.include_router(health.router, tags=["Health"])
app.include_router(sites.router, prefix="/sites", tags=["Sites"])
app.include_router(simulation.router, prefix="/simulation", tags=["Simulation"])
app.include_router(diagnostics.router, prefix="/diagnostics", tags=["Diagnostics"])
app.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
app.include_router(exports.router, prefix="/exports", tags=["Exports"])
