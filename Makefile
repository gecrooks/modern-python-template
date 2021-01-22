
# Kudos: Adapted from Auto-documenting default target
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

.DEFAULT_GOAL := help

FILES = hooks

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'


test:
	rm -rf example_python_project/.git  # Remove old git test repo if previously initilized	
	cookiecutter  --no-input --overwrite-if-exists .
	cd example_python_project; make all
	cd example_python_project; make clean
	rm -rf example_python_project/.git  # Not needed 	


.PHONY: help
.PHONY: test	
