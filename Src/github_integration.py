from github import Github
import logging

class GitHubIntegration:
    def __init__(self, repo_url: str, branch: str, token: str):
        """Initialize GitHub integration"""
        self.repo_url = repo_url
        self.branch = branch
        self.token = token
        self.logger = logging.getLogger(__name__)
        
        self.g = Github(self.token)
        self.repo = self.g.get_repo(repo_url.split('github.com/')[-1].replace('.git', ''))
        self.logger.info("GitHubIntegration initialized")

    def push_changes(self, file_path: str, commit_message: str):
        """Example method showing integration"""
        with open(file_path, 'r') as file:
            content = file.read()
        
        self.repo.create_file(
            path=file_path.split('/')[-1],
            message=commit_message,
            content=content,
            branch=self.branch
        )
        self.logger.info(f"Pushed changes to {self.branch}")