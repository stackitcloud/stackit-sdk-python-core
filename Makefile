install:
	pip install .
install-dev:
	pip install .[dev]
test:
	pytest
lint:
	flake8 .