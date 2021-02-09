
# Kudos: Adapted from Auto-documenting default target
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

.DEFAULT_GOAL := help

NAME = example_python_project
FILES = $(NAME) docs/conf.py setup.py

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

all: about coverage lint typecheck docs build   ## Run all tests

test:		## Run unittests
	pytest --disable-pytest-warnings

coverage:	## Report test coverage
	@echo
	pytest --disable-pytest-warnings --cov
	@echo

lint:		## Lint check python source
	@isort --check $(NAME)  ||  echo "isort:   FAILED!"
	@black --check --quiet $(NAME)    || echo "black:   FAILED!"
	@flake8 $(FILES)

delint:   ## Run isort and black to delint project
	@echo	
	isort $(NAME)
	@echo
	black $(NAME)
	@echo

typecheck:	## Static typechecking 
	mypy $(NAME)

docs:		## Build documentation
	(cd docs; make html)

docs-open:  ## Build documentation and open in webbrowser
	(cd docs; make html)
	open docs/_build/html/index.html

docs-clean: 	## Clean documentation build
	(cd docs; make clean)

pragmas:	## Report all pragmas in code
	@echo "** Pragma for test coverage **"
	@grep 'pragma: no cover' --color -r -n $(FILES) || echo "No Typecheck Pragmas"
	@echo
	@echo "** flake8 linting pragmas **"
	@echo "(http://flake8.pycqa.org/en/latest/user/error-codes.html)"
	@grep '# noqa:' --color -r -n $(FILES) || echo "No flake8 pragmas"
	@echo
	@echo "** Typecheck pragmas **"
	@grep '# type:' --color -r -n $(FILES) || echo "No Typecheck Pragmas"

about:	## Report versions of dependent packages
	@python -m $(NAME).about

status:  ## git status --short --branch
	@git status --short --branch

build: ## Setuptools build
	./setup.py clean --all
	./setup.py sdist bdist_wheel

clean: ## Clean up after setuptools
	./setup.py clean --all

requirements: ## Make requirements.txt
	pip freeze > requirements.txt


.PHONY: help
.PHONY: docs
.PHONY: build
