#!/bin/bash

# Activate virtual environment
source venv/bin/activate  # cSpell:ignore venv

# Change to project directory
cd ci-cd-pipeline-project

# Run the Flask application
python src/app.py