#!/bin/bash

echo "Setting up GitHub Microservice Deployment..."

# Update system
sudo apt-get update

# Install required packages
sudo apt-get install -y python3-full python3-pip python3-venv

# Create virtual environment
python3 -m venv venv  # cSpell:ignore venv

# Activate virtual environment and install packages
source venv/bin/activate  # cSpell:ignore venv
pip install -r requirements.txt

echo "Setup complete! To run the application:"
echo "1. source venv/bin/activate"  # cSpell:ignore venv
echo "2. cd ci-cd-pipeline-project"
echo "3. python src/app.py"