black:
	black src

isort:
	isort src

ruff-check:
	ruff check src

ruff-format:
	ruff check src --fix

format: isort black ruff-format
