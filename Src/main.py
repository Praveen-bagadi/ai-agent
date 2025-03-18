import sys
import os
import logging
from dotenv import load_dotenv
import gradio as gr

# Ensure src/ directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import AI agent modules
from src.upwork_bot import UpworkBot
from src.adf_monitor import ADFMonitor
from src.email_alerts import EmailAlerts
from src.github_integration import GitHubIntegration
from src.webui import WebUI  # Gradio-based UI

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    filename="logs/ai_agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def start_ai_agent():
    """Initialize and start all AI agent modules."""
    try:
        logging.info("Starting AI Agent...")

        # Initialize AI Agent Modules
        upwork_bot = UpworkBot()
        adf_monitor = ADFMonitor()
        email_alerts = EmailAlerts()
        github_integration = GitHubIntegration()

        # Start Gradio WebUI
        web_ui = WebUI(upwork_bot, adf_monitor, email_alerts, github_integration)
        web_ui.launch()

    except Exception as e:
        logging.error(f"Error in AI Agent: {str(e)}", exc_info=True)
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    start_ai_agent()
