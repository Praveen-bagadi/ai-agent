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