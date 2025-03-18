import os
import logging
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set up logging
logging.basicConfig(
    filename="logs/adf_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ADFMonitor:
    def __init__(self):
        """Initialize Azure Data Factory Monitoring"""
        self.subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
        self.resource_group = os.getenv("AZURE_RESOURCE_GROUP")
        self.adf_name = os.getenv("AZURE_ADF_NAME")

        # Authenticate with Azure
        self.credential = DefaultAzureCredential()
        self.client = DataFactoryManagementClient(self.credential, self.subscription_id)

    def check_pipeline_status(self, pipeline_name):
        """Check the latest run status of a pipeline"""
        logging.info(f"Checking status for pipeline: {pipeline_name}")

        pipeline_runs = list(self.client.pipeline_runs.list_by_factory(
            self.resource_group, self.adf_name
        ))

        for run in pipeline_runs:
            if run.pipeline_name == pipeline_name:
                logging.info(f"Latest Status for {pipeline_name}: {run.status}")
                return run.status
        return "Unknown"

    def restart_pipeline(self, pipeline_name):
        """Restart a failed pipeline"""
        logging.info(f"Restarting pipeline: {pipeline_name}")

        run_response = self.client.pipelines.create_run(
            self.resource_group, self.adf_name, pipeline_name
        )

        logging.info(f"Pipeline {pipeline_name} restarted with Run ID: {run_response.run_id}")

    def monitor_and_restart(self):
        """Monitor and restart failed pipelines"""
        pipelines_to
