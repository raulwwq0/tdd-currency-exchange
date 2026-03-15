.PHONY: setup install test test-watch coverage clean help

# Python and virtual environment configuration
PYTHON := python3
VENV := .venv
BIN := $(VENV)/bin
PYTHON_VENV := $(BIN)/python
PIP := $(BIN)/pip

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

setup: ## Create virtual environment and install dependencies
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo ""
	@echo "Virtual environment created successfully!"
	@echo "To activate it, run: source $(VENV)/bin/activate"

install: ## Install dependencies (requires active venv)
	pip install -r requirements.txt

test: ## Run all tests
	pytest tests/ -v

test-watch: ## Run tests in watch mode
	pytest-watch tests/ -v

coverage: ## Run tests with coverage report
	pytest tests/ --cov=src --cov-report=html --cov-report=term

clean: ## Remove virtual environment and cache files
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
