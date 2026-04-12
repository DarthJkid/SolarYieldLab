# PV Modelling Methodology

## DC Model
Uses the PVWatts v5 model implemented via pvlib:
- SAPM (Sandia Array Performance Model) cell temperature
- Simple efficiency model

## AC Conversion
- Inverter efficiency: 96% (default)
- System losses: 14% (default, configurable)

## Validation
Simulated yield compared against observed generation data
using RMSE, MAE, and MBE metrics.
