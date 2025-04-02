import os
import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

class ConfigManager:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        try:
            with open(self.config_path) as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Config file not found at {self.config_path}")
            return {}
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in config file {self.config_path}")
            return {}
        except Exception as e:
            logger.error(f"Config load failed: {str(e)}")
            return {}

    def get(self, key: str, default: Any = None) -> Any:
        """Get config value using dot notation"""
        keys = key.split("/")
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value if value != {} else default

def validate_env_vars(required_vars: list) -> bool:
    """Check required environment variables"""
    missing = [var for var in required_vars if var not in os.environ]
    if missing:
        logger.error(f"Missing env vars: {', '.join(missing)}")
        return False
    return True

def load_environment(env_path: Optional[Path] = None) -> bool:
    """Load environment variables"""
    env_path = env_path or Path(".env")
    try:
        if not env_path.exists():
            logger.warning(f"Env file not found: {env_path}")
            return False
        load_dotenv(env_path)
        return True
    except Exception as e:
        logger.error(f"Failed to load environment: {str(e)}")
        return False