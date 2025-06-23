#!/bin/bash
set -e  # Exit on error

echo "Creating Python virtual environment"
python3 -m venv .venv

echo "Activating virtual environment"
source .venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Installing pytest plugin in editable mode..."
pip install -e .

echo "source .venv/bin/activate"
