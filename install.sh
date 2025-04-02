#!/bin/bash

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install package in editable mode
pip install -e .

# Install Playwright browsers
playwright install

# Set up configuration directory
CONFIG_DIR="$HOME/.config/ai-agent"
mkdir -p "$CONFIG_DIR"

# Copy example files if they don't exist
[ -f "$CONFIG_DIR/config.json" ] || cp config.json "$CONFIG_DIR/"
[ -f "$CONFIG_DIR/.env" ] || cp .env.example "$CONFIG_DIR/.env"

echo "Installation complete!"
echo "Please edit your configuration files in: $CONFIG_DIR"
echo "Run with: ai-agent"