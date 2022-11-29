
# Kudos: Adapted from Auto-documenting default target
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

.DEFAULT_GOAL := help

NAME = example_python_project
FILES = $(NAME) docsrc/conf.py setup.py

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

about:  ## Report versions of dependent packages
	@python -m $(NAME).about

status:  ## git status --short --branch
	@git status --short --branch

init:  ## Install package ready for development
	python -m pip install --upgrade pip
	if [ -f requirements.txt ]; then python -m pip install -r requirements.txt; fi         
	python -m pip install -e .[dev]
	python -m pre-commit install  # Install git pre-commit hook

all: about coverage lint typecheck docs build   ## Run all tests

test:  ## Run unittests
	python -m pytest --disable-pytest-warnings

coverage:  ## Report test coverage
	@echo
	python -m pytest --disable-pytest-warnings --cov $(NAME)
	@echo

lint:  ## Lint check python source
	@python -m isort --check $(NAME)  ||  echo "isort:   FAILED!"
	@python -m black --check --quiet $(NAME)    || echo "black:   FAILED!"
	@python -m flake8 $(FILES)

delint:  ## Run isort and black to delint project
	@echo	
	python -m isort $(NAME)
	@echo
	python -m black $(NAME)
	@echo

typecheck:  ## Static typechecking 
	python -m mypy $(NAME)

docs:  ## Build documentation
	(cd docsrc; make html)

docs-open:  ## Build documentation and open in webbrowser
	(cd docsrc; make html)
	open docsrc/_build/html/index.html

docs-clean:  ## Clean documentation build
	(cd docsrc; make clean)

docs-github-pages: docs  ## Install html in docs directory ready for github pages
	# https://www.docslikecode.com/articles/github-pages-python-sphinx/
	@mkdir -p docs
	@touch docs/.nojekyll  # Tell github raw html, not jekyll
	@cp -a _build/html/. ../docs

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

build:  ## Setuptools build
	./setup.py --quiet clean --all
	./setup.py --quiet sdist bdist_wheel

clean:  ## Clean up after setuptools
	./setup.py clean --all

requirements:  ## Make requirements.txt
	python -m pip freeze > requirements.txt


.PHONY: help
.PHONY: docs
.PHONY: build
