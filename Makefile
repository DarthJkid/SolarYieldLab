.PHONY: install install-dev lint test run-app docker-build docker-up clean

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	pre-commit install

lint:
	ruff check src app scripts tests
	black --check src app scripts tests

test:
	pytest tests/ --cov=src --cov-report=html -v

run-app:
	streamlit run app/Home.py

docker-build:
	docker compose build

docker-up:
	docker compose up -d

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -rf .pytest_cache htmlcov .coverage dist build
