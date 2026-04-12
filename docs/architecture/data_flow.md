# Data Flow

```
External APIs
  │  NASA POWER / PVWatts / PVGIS / NSRDB / ERA5 / CAMS
  ▼
Ingestion Layer (src/ingestion/)
  │  Clients → Parsers → Raw store (data/raw/)
  ▼
Validation (src/validation/)
  │  Schema / units / physical plausibility
  ▼
Processing (src/processing/)
  │  Time alignment → Harmonisation → Feature engineering
  ▼
Feature Store (data/feature_store/)
  ▼
Simulation (src/simulation/)   ML Models (src/ml/)
  │                                    │
  └──────────── Analytics (src/analytics/) ──┘
                          │
                    Reporting / API / App
```
