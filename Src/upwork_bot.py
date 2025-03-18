import os
import time
import logging
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from src.utils import generate_ai_proposal

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    filename="logs/upwork_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class UpworkBot:
    def __init__(self):
        """Initialize Upwork bot settings."""
        self.upwork_url = "https://www.upwork.com/"
        self.email = os.getenv("UPWORK_EMAIL")
        self.password = os.getenv("UPWORK_PASSWORD")
        self.headless = False  # Change to True for headless mode

    def login(self, page):
        """Logs into Upwork account."""
        logging.info("Logging into Upwork...")
        page.goto(self.upwork_url)
        
        # Click on Login Button
        page.click("text=Log In")

        # Fill email & password
        page.fill("input[name='username']", self.email)
        page.fill("input[name='password']", self.password)

        # Submit login form
        page.click("text=Sign In")
        time.sleep(5)  # Wait for login to complete

        logging.inf
