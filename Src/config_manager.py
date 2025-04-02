from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)

def get_config_path() -> Path:
    """Find config file in standard locations"""
    search_paths = [
        Path.home() / ".config" / "ai-agent" / "config.json",  # Linux/macOS
        Path.home() / "AppData" / "Local" / "ai-agent" / "config.json",  # Windows
        Path("config.json"),  # Current directory
    ]
    
    for path in search_paths:
        if path.exists():
            logger.info(f"Using config file: {path}")
            return path
    
    logger.warning("No config file found, using defaults")
    return Path(__file__).parent.parent / "config.json"

def get_env_path() -> Path:
    """Find .env file in standard locations"""
    search_paths = [
        Path.home() / ".config" / "ai-agent" / ".env",
        Path.home() / "AppData" / "Local" / "ai-agent" / ".env",
        Path(".env"),
    ]
    
    for path in search_paths:
        if path.exists():
            logger.info(f"Using environment file: {path}")
            return path
    
    return Path(__file__).parent.parent / ".env"