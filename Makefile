.PHONY: setup install test test-watch coverage lint lint-fix format typecheck check clean help

# Python and virtual environment configuration
PYTHON := python3
VENV := .venv
BIN := $(VENV)/bin
PYTHON_VENV := $(BIN)/python
PIP := $(BIN)/pip
PYTEST := $(BIN)/pytest
PYTEST_WATCH := $(BIN)/pytest-watch
RUFF := $(BIN)/ruff
PYRIGHT := $(BIN)/pyright

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
	PYTHONPATH=. $(PYTEST) tests/ -v

test-watch: ## Run tests in watch mode
	PYTHONPATH=. $(PYTEST_WATCH) tests/ -v

coverage: ## Run tests with coverage report
	PYTHONPATH=. $(PYTEST) tests/ --cov=src --cov-report=html --cov-report=term

lint: ## Run ruff linter
	$(RUFF) check src tests

lint-fix: ## Auto-fix linting issues with ruff
	$(RUFF) check --fix src tests

format: ## Format code with ruff
	$(RUFF) format src tests

format-check: ## Check code formatting without making changes
	$(RUFF) format --check src tests

typecheck: ## Run pyright type checker
	$(PYRIGHT)

check: lint format-check typecheck ## Run all checks (lint, format-check, typecheck)

clean: ## Remove virtual environment and cache files
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
