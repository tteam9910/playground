
clear-project:
	rm -rf .venv


install-project:
	poetry install
	poetry run pre-commit install


test:
	poetry run pytest tests/
