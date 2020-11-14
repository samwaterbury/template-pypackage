.DEFAULT_GOAL := help
.PHONY: help

clean: ## Remove generated files
clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.py[co]' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-test:
	rm -fr .pytest_cache/
	rm -fr .coverage
	rm -rf .tox/

env: ## Create or update conda environment
	conda env create --file environment.yaml 2>/dev/null \
		|| conda env update --file environment.yaml --prune

lint: ## Lint all Python files
	isort . && black .

test: ## Run tests and generate coverage report on success
	coverage run -m pytest && coverage report

help: ## Show available commands
	@echo "usage: make [target] ..."
	@echo
	@echo "targets:"
	@egrep "^(.+)\:\ ##\ (.+)" ${MAKEFILE_LIST} | column -t -c 2 -s ":#"
