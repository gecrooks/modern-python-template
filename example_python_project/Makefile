
# Kudos: Adapted from Auto-documenting default target
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

.DEFAULT_GOAL := help

NAME = example_python_project
FILES = $(NAME) docsrc/conf.py setup.py

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'


.PHONY: about
about:  ## Report versions of dependent packages
	@python -m $(NAME).about


.PHONY: status
status:  ## git status --short --branch
	@git status --short --branch

.PHONY: init
init:  ## Install package ready for development
	python -m pip install --upgrade pip
	if [ -f requirements.txt ]; then python -m pip install -r requirements.txt; fi         
	python -m pip install -e .[dev]
	python -m pre-commit install  # Install git pre-commit hook


.PHONY: all
all: about coverage lint typecheck docs build  ## Run all tests

.PHONY: test
test:  ## Run unittests
	python -m pytest --disable-pytest-warnings

.PHONY: coverage
coverage:  ## Report test coverage
	@echo
	python -m pytest --disable-pytest-warnings --cov $(NAME)
	@echo

.PHONY: lint
lint:  ## Lint check python source
	@python -m isort --check $(NAME)  ||  echo "isort:   FAILED!"
	@python -m black --check --quiet $(NAME)    || echo "black:   FAILED!"
	@python -m flake8 $(FILES)

.PHONY: delint
delint:  ## Run isort and black to delint project
	@echo	
	python -m isort $(NAME)
	@echo
	python -m black $(NAME)
	@echo

.PHONY: typecheck
typecheck:  ## Static typechecking 
	python -m mypy $(NAME)

.PHONY: precommit
precommit: ## Run all pre-commit hooks
	pre-commit run --all

.PHONY: docs
docs:  ## Build documentation
	(cd docsrc; make html)

.PHONY: docs-open
docs-open:  ## Build documentation and open in webbrowser
	(cd docsrc; make html)
	open docsrc/_build/html/index.html

.PHONY: docs-clean
docs-clean:  ## Clean documentation build
	(cd docsrc; make clean)

.PHONY: docs-github-pages
docs-github-pages: docs  ## Install html in docs directory ready for github pages
	# https://www.docslikecode.com/articles/github-pages-python-sphinx/
	@mkdir -p docs
	@touch docs/.nojekyll  # Tell github raw html, not jekyll
	@cp -a _build/html/. ../docs

.PHONY: pragmas
pragmas:  ## Report all pragmas in code
	@echo "** Test coverage pragmas**"
	@grep 'pragma: no cover' --color -r -n $(FILES) || echo "No test coverage pragmas"
	@echo
	@echo "** Linting pragmas **"
	@echo "(http://flake8.pycqa.org/en/latest/user/error-codes.html)"
	@grep '# noqa:' --color -r -n $(FILES) || echo "No linting pragmas"
	@echo
	@echo "** Typecheck pragmas **"
	@grep '# type:' --color -r -n $(FILES) || echo "No typecheck pragmas"

.PHONY: build
build:  ## Build a phython soruce distribution and wheel
	python -m build


.PHONY: requirements
requirements:  ## Make requirements.txt
	python -m pip freeze > requirements.txt
