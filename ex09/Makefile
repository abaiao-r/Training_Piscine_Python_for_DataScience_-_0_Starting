VENV := venv
PKG := ft_package
PYTHON := python3.10

.PHONY: clean build install test

clean:
	rm -rf dist build *.egg-info $(VENV)
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	-$(PYTHON) -m pip uninstall -y $(PKG)

build: $(VENV)
	$(VENV)/bin/pip install --upgrade pip setuptools wheel build
	$(VENV)/bin/$(PYTHON) -m build

install: clean build
	$(VENV)/bin/pip install $(shell ls dist/*.whl | head -n 1)

test: install
	$(VENV)/bin/$(PYTHON) tester.py

$(VENV):
	$(PYTHON) -m venv $(VENV)
