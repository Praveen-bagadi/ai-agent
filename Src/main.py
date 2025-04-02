import sys
import logging
from pathlib import Path
from utils import ConfigManager, load_environment, validate_env_vars
from recording_manager import RecordingManager
import sys
import os
import logging
from pathlib import Path
import os
import sys
from pathlib import Path
from .main import start_ai_agent
from .config_manager import get_config_path, get_env_path

def main():
    # Set up default configuration paths
    config_path = get_config_path()
    env_path = get_env_path()
    
    if not env_path.exists():
        print("Warning: .env file not found. Using system environment variables.")
    
    start_ai_agent(config_path=config_path, env_path=env_path)

if __name__ == "__main__":
    main()

try:
    from utils import ConfigManager, load_environment
    config = ConfigManager("config.yaml")
    if not config.config:  # If config is empty
        config = ConfigManager()  # Fallback to defaults
except Exception as e:
    logging.warning(f"Config loading issue: {str(e)}")
    config = type('SimpleConfig', (), {'get': lambda self, k, d=None: d})()  # Dummy config
# Initialize core components
config = ConfigManager()
recording_manager = RecordingManager()

# Import agent components
from upwork_bot import UpworkBot
from adf_monitor import ADFMonitor
from email_alerts import EmailAlerts
from github_integration import GitHubIntegration
from webui import WebUI

def configure_logging():
    logging.basicConfig(
        filename="logs/ai_agent.log",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filemode="a"
    )

def initialize_components():
    """Initialize all agent components with dependency injection"""
    components = {
        "upwork": UpworkBot(
            email=os.getenv("UPWORK_EMAIL"),
            password=os.getenv("UPWORK_PASSWORD"),
            config=config
        ),
        "adf": ADFMonitor(
            subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"),
            resource_group=os.getenv("AZURE_RESOURCE_GROUP"),
            factory_name=os.getenv("AZURE_FACTORY_NAME"),
            config=config
        ),
        "email": EmailAlerts(
            smtp_server=os.getenv("SMTP_SERVER"),
            smtp_port=int(os.getenv("SMTP_PORT")),
            smtp_user=os.getenv("SMTP_USER"),
            smtp_pass=os.getenv("SMTP_PASSWORD"),
            receiver_email=os.getenv("RECEIVER_EMAIL"),
            config=config
        ),
        "github": GitHubIntegration(
            repo_url=os.getenv("GITHUB_REPO"),
            branch=os.getenv("GITHUB_BRANCH"),
            token=os.getenv("GITHUB_TOKEN"),
            config=config
        ),
        "recording": recording_manager
    }
    return components

def start_ai_agent():
    """Main entry point for the AI agent"""
    try:
        if not load_environment():
            raise RuntimeError("Failed to load environment variables")
            
        required_vars = [
            'AZURE_SUBSCRIPTION_ID',
            'UPWORK_EMAIL',
            'GITHUB_TOKEN'
        ]
        if not validate_env_vars(required_vars):
            raise EnvironmentError("Missing required environment variables")

        components = initialize_components()
        WebUI(**components).launch(server_port=7860)

    except Exception as e:
        logging.critical(f"AI Agent failed to start: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    configure_logging()
    start_ai_agent()