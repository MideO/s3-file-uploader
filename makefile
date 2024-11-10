# Help Text
help: ## Show this help.
    # From https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
    # List of documented commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


# End Help Text
STORAGE_PATH=${GITHUB_WORKSPACE:-/shared_data/}
# Linting
lint: ## Run black formatter and pylint
	@python3 -m flake8 s3fileuploader features
	@python3 -m black s3fileuploader features
	@python3 -m pylint s3fileuploader features
# End Linting

# Install Requirements
install-requirements: ## Run Install All Requirements
	@pip3 install -r requirements-all.txt

# End Install Requirements

# Local Stack Start
devstack-up: ## Run docker compose stack
	@docker compose up --build -d

devstack-logs: ## Spool Logs
	@echo "\nDev Stack Logs\n"
	@echo "redis logs"
	@echo "============="
	@docker logs redis
	@echo "\nmoto logs"
	@echo "============="
	@docker logs moto
	@echo "\ncelery-worker-1 logs"
	@echo "===================="
	@docker logs celery-worker-1
	@echo "\ncelery-worker-2 logs"
	@echo "===================="
	@docker logs celery-worker-2
	@echo "\ncelery-worker-2 logs"
	@echo "===================="
	@docker logs s3-file-uploader
	@echo "\n"
devstack-down: ## Tear down docker compose stack
	@docker compose down  --volumes --remove-orphans
# Local Stack End


# Testing
.PHONY: test
test: ## Run pytest with coverage
	@python3 -m pytest -v --cov=s3fileuploader --cov-report term-missing s3fileuploader/tests

feature-test: ## Run behave feature tests
	@python3 -m behave


test-all: ## Run end to end tests
	@make install-requirements lint test devstack-up feature-test devstack-logs devstack-down
# Testing End