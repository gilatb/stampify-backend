web:
	. run.bash

revision:
	alembic revision -m "$(m)" --autogenerate

requirements:
	pip install -r requirements.txt

start: requirements web

test:
	pytest --cov=backend --cov-fail-under 100 --blockage --cov-report term-missing

coverage-collect:
	coverage run -m pytest

coverage-report:
	coverage html

coverage: coverage-collect coverage-report

mypy:
	mypy backend tests *.py

flake8:
	flake8 .

pycln:
	pycln .

isort:
	isort .

bandit:
	bandit -q -r -x /venv,/tests .

check: isort flake8 mypy bandit test
