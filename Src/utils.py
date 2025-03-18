import os
import logging
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging Setup
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "ai_agent.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_message(message, level="info"):
    """Logs messages at different levels."""
    levels = {
        "info": logging.info,
        "warning": logging.warning,
        "error": logging.error,
        "debug": logging.debug
    }
    levels.get(level, logging.info)(message)

def load_config(config_file="config.json"):
    """Loads configuration from a JSON file."""
    if not os.path.exists(config_file):
        log_message(f"Config file {config_file} not found!", "error")
        return {}

    with open(config_file, "r") as file:
        config = json.load(file)
    log_message(
