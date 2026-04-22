TEMPLATE_DIR := ../templates/problem
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
	@echo "Created $(CURDIR)/$(NAME)"

%:
	@:
