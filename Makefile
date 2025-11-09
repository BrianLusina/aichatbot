# Define colors
RED=\033[0;31m
GREEN=\033[0;32m
YELLOW=\033[0;33m
BLUE=\033[0;34m
# No Color
NC=\033[0m

################################################## Utility Commands ########################################################
.PHONY: help
help: ## This help dialog describing all commands
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%-30s %s\n" "target" "help" ; \
	printf "%-30s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-30s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done

################################################## Application Commands ########################################################

.PHONY: run
run: ## Runs the project
	@echo "${GREEN} Running application on port $(PORT)${NC}"
	cd src && python main.py

.PHONY: build
build: ## builds project
	uv build

.PHONY: ty-check
ty-check: ## type check with ty
	uv run ty check

.PHONY: pyrefly-check
pyrefly-check: ## type check with pyrefly
	uv run pyrefly check

lint-ruff: ## check lint errors with ruff
	ruff check

format: ## format with Ruff
	ruff format