import requests


from repository.settings import GITHUB_REPOS_API_URL


class RepositoryInterface:

    def fetch_owner(self, user, repo):
        raise NotImplementedError

    def fetch_commits(self, user, repo):
        raise NotImplementedError


class GithubRequestHandler(RepositoryInterface):

    def __call__(self, user, repo):
        repo_url = self.build_repository_url(user, repo)
        return self.make_api_call(repo_url)

    def build_repository_url(self, user, repo):
        return self.format_url(user, repo)

    def format_url(self, user, repo):
        return "{}/{}/{}".format(GITHUB_REPOS_API_URL, user, repo)

    def make_api_call(self, resource_link):
        response = requests.get(url=resource_link).json()
        return response

    def fetch_owner(self, user, repo):
        repo_url = self.build_repository_url(user, repo)
        response = self.make_api_call(repo_url)
        return response["owner"]

    def fetch_commits(self, user, repo):
        repo_url = self.build_repository_url(user, repo)
        response = self.make_api_call(repo_url)
        commits = self.make_api_call(response["commits_url"][:-6])
        return commits
