install:
	pip install .
install-dev:
	poetry install --only dev --no-root; pip install -e .
test:
	pytest
lint:
	flake8 .