# Help Text
define HELP_TEXT
Available Tasks
 - help: Print all available tasks
 - install-requirements: Install all pip requirements
 - lint: run pylint
 - test: Run unit tests with pytest
 - devstack-up: Run docker compose stack
 - devstack-down: Bring down docker compose stack
 - feature-test: Run all behave feature tests
 - test-all:
         - Run docker compose stack
         - Run All Tests
         - Bring down docker compose stack

endef

export HELP_TEXT
help:
	@echo "$$HELP_TEXT"
# End Help Text

# Linting
lint:
	@black s3fileuploader features
	@pylint s3fileuploader features
# End Linting

# Install Requirements
install-requirements:
	@pip3 install -r requirements-all.txt

# End Install Requirements

# Local Stack Start
devstack-up:
	@docker compose up --build -d

devstack-down:
	@docker compose down  --volumes --remove-orphans
# Local Stack End


# Testing
.PHONY: test
test:
	@pytest -v --cov=s3fileuploader --ignore=tests --cov-report term-missing

feature-test:
	@behave

test-all: install-requirements lint test devstack-up feature-test devstack-down
# Testing End