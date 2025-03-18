How to Run the WebUI1️⃣ Activate Virtual Environment

source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
2️⃣ Install Dependencies

pip install -r requirements.txt
3️⃣ Run the WebUI

python src/webui.py
4️⃣ Open in Browser
The Gradio WebUI will launch automatically at
➡️ http://127.0.0.1:7860

How to Use in Python
In your scripts (adf_monitor.py, email_alerts.py, etc.), you can load this config using:

from src.utils import load_config

config = load_config()

# Access ADF config
factory_name = config["adf"]["factory_name"]

# Access email settings
smtp_server = config["email"]["smtp_server"]

# Access GitHub repo details
repo_url = config["github"]["repo_url"]

Security Best Practices
✅ DO NOT commit .env to GitHub – add it to .gitignore
✅ Use GitHub Secrets for CI/CD pipelines
✅ Keep API tokens secure and refresh periodically
1️⃣ Install python-dotenv (if not installed)

pip install python-dotenv
2️⃣ Load Environment Variables in Python

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access variables
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
smtp_server = os.getenv("SMTP_SERVER")
github_token = os.getenv("GITHUB_TOKEN")

print(f"Using Subscription ID: {subscription_id}")

How to Install Dependencies
Run the following command in your virtual environment:

pip install -r requirements.txt

Installation

1. Clone the Repository

git clone https://github.com/Praveen-bagadi/ai-agent.git
cd ai-agent

2. Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

3. Configure Environment Variables

Create a .env file and add the necessary credentials:

AZURE_SUBSCRIPTION_ID=your-subscription-id
AZURE_RESOURCE_GROUP=your-resource-group
AZURE_FACTORY_NAME=your-adf-factory-name
SMTP_SERVER=smtp.example.com
GITHUB_TOKEN=your-github-token
UPWORK_EMAIL=your-email@example.com

4. Run the AI Agent

To start the WebUI:

python src/webui.py

For CLI execution:

python src/main.py

Usage

Access the WebUI at http://localhost:7860 to control automation tasks

Monitor ADF Pipelines automatically or manually restart failed pipelines

Send Upwork Proposals directly from the interface

Trigger GitHub actions like commits and pushes

Receive Email Alerts for pipeline failures

Contribution

Feel free to contribute by submitting issues or pull requests.
