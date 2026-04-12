# Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|-----------|--------|-----------|
| R01 | API rate limiting | Medium | High | Caching layer |
| R02 | Model overfit | Medium | Medium | Cross-validation + held-out test set |
| R03 | Data source discontinuation | Low | High | Multi-source fallback strategy |
| R04 | PII in observed data | Low | High | Data anonymisation pipeline |
