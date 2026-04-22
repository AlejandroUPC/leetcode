TEMPLATE_DIR := templates/problem
TEMPLATE_P_DIR := templates/pattern
NAME := $(word 2,$(MAKECMDGOALS))

.PHONY: new

new:
	@if [ -z "$(NAME)" ]; then \
		echo "Usage: make new 001-two-sum"; \
		exit 1; \
	fi
	@if [ -e "$(NAME)" ]; then \
		echo "Error: $(NAME) already exists."; \
		exit 1; \
	fi
	@cp -R "$(TEMPLATE_DIR)" "$(NAME)"
	@echo "Created $(NAME)"

newp:
	@if [ -z "$(NAME)" ]; then \
		echo "Usage: make newp two-pointer"; \
		exit 1; \
	fi
	@if [ -e "patterns/$(NAME)" ]; then \
		echo "Error: patterns/$(NAME) already exists."; \
		exit 1; \
	fi
	@cp -R "$(TEMPLATE_P_DIR)" "patterns/$(NAME)"
	@echo "Created pattern patterns/$(NAME)"

.PHONY: tests

tests:
	@set -eu; \
	tests="$$(find . -type f -name 'test.py' ! -path './.git/*' ! -path './.venv/*' ! -path './venv/*' ! -path '*/__pycache__/*' ! -path './templates/*')"; \
	if [ -z "$$tests" ]; then echo "No test.py files found."; exit 1; fi; \
	for f in $$tests; do \
		echo "==> $$f"; \
		if python3 "$$f"; then echo "OK: $$f"; else echo "FAIL: $$f"; exit 1; fi; \
	done; \
	echo "ALL OK"

%:
	@:
