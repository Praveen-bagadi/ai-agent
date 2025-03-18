import os
import logging
from github import Github
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    filename="logs/github_integration.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class GitHubIntegration:
    def __init__(self):
        """Initialize GitHub API connection"""
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.repo_name = os.getenv("GITHUB_REPO")

        self.github_client = Github(self.github_token)
        self.repo = self.github_client.get_repo(self.repo_name)

    def commit_and_push(self, file_path, commit_message):
        """Commit and push changes to GitHub"""
        try:
            with open(file_path, "r") as file:
                content = file.read()

            file_name = os.path.basename(file_path)
            existing_file = None

            # Check if file already exists
            try:
                existing_file = self.repo.get_contents(file_name)
            except:
                pass  # File does not exist

            if existing_file:
                self.repo.update_file(existing_file.path, commit_message, content, existing_file.sha)
                logging.info(f"Updated file: {file_name}")
            else:
                self.repo.create_file(file_name, commit_message, content)
                logging.info(f"Created new file: {file_name}")

        except Exception as e:
            logging.error(f"GitHub commit failed: {str(e)}")

    def create_pull_request(self, branch_name, title, body):
        """Create a pull request on GitHub"""
        try:
            pr = self.repo.create_pull(title=title, body=body, head=branch_name, base="main")
            logging.info(f"Pull request created: {pr.html_url}")
        except Exception as e:
            logging.error(f"Failed to create pull request: {str(e)}")

if __name__ == "__main__":
    github_bot = GitHubIntegration()
    github_bot.commit_and_push("src/example.py", "Added new feature")
    github_bot.create_pull_request("feature-branch", "New Feature", "Added automation for X")
