# MLOps Lifecycle

## Training Pipeline
1. Feature extraction from feature store
2. Model training with cross-validation
3. Experiment tracking via MLflow
4. Model registration in MLflow registry

## Serving Pipeline
1. Load production model from registry
2. Run batch inference on new data
3. Store predictions in processed store

## Monitoring
1. Drift detection on input features
2. Performance monitoring vs. observed generation
3. Automated retraining trigger via Prefect schedule
