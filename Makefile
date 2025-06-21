# Makefile for the OpenGL Textured Quad Demo

# Define the Python interpreter, especially if using a virtual environment
PYTHON = python

# Default target (optional, can be 'run' or 'all')
default: run

# Target to install dependencies
install: requirements.txt
	$(PYTHON) -m pip install -r requirements.txt
	@echo "Dependencies installed."

# Target to run the application
run:
	$(PYTHON) main.py

# Target to check PEP8 compliance
lint:
	$(PYTHON) -m autopep8 --diff --recursive .
	@echo "Linting check complete. Differences (if any) are shown above."

# Target to automatically format code using autopep8
format:
	$(PYTHON) -m autopep8 --in-place --recursive .
	@echo "Code formatting complete."

# Phony targets are not files
.PHONY: default install run lint format
