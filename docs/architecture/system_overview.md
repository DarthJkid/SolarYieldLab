# System Overview

SolarYieldLab is a modular platform for solar yield simulation, diagnostics,
and research. It integrates multiple external data sources, a PV physics engine,
ML models for residual estimation and anomaly detection, and a Streamlit dashboard.

## High-Level Components

| Layer | Component | Technology |
|-------|-----------|------------|
| Data Ingestion | Multi-source clients | Python / requests |
| Processing | Harmonisation & feature engineering | pandas / numpy |
| Simulation | PV yield physics | pvlib |
| ML | Surrogate, residual, anomaly models | scikit-learn / mlflow |
| Orchestration | Pipeline scheduling | Prefect |
| API | REST endpoints | FastAPI |
| Dashboard | Interactive UI | Streamlit |
