.PHONY: init-repo-setup poetry-export test lint precommit

init-repo-setup:
	poetry install --all-groups
	pre-commit install

poetry-export-dev:
	poetry export --with dev --without-hashes -f requirements.txt -o requirements_dev.txt

poetry-export-prod:
	poetry export --without-hashes -f requirements.txt -o requirements.txt

lint:
	flake8 langunittest

precommit:
	pre-commit
