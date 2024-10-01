.PHONY: install migrate makemigrations run-server createsuperuser shell test coverage lint
install:
	poetry install

migrate:
	poetry run python -m core.manage migrate

makemigrations:
	poetry run python -m core.manage makemigrations

run-server:
	poetry run python -m core.manage runserver

createsuperuser:
	poetry run python -m core.manage createsuperuser

shell:
	poetry run python -m core.manage shell

test:
	poetry run python -m core.manage test

coverage:
	poetry run coverage run --source='.' -m core.manage test
	poetry run coverage report

lint:
	poetry run flake8 .