from django.urls import path

from repository.github_request_handler import GithubRequestHandler
from .views import RepoDetails, RepoOwnerDetails, RepoCommitsDetails

urlpatterns = [
    path('repo/', RepoDetails.as_view(
        repo_api_handler=GithubRequestHandler()
    )),
    path('repo/<owner>/<repository>/', RepoDetails.as_view(
        repo_api_handler=GithubRequestHandler()
    )),
    path('repoOwner/', RepoOwnerDetails.as_view(
        repo_api_handler=GithubRequestHandler()
    )),
    path('repoOwner/<owner>/<repository>/', RepoOwnerDetails.as_view(
        repo_api_handler=GithubRequestHandler()
    )),
    path('repoCommits/', RepoCommitsDetails.as_view(
        repo_api_handler=GithubRequestHandler()
    )),
    path('repoCommits/<owner>/<repository>/', RepoCommitsDetails.as_view(
        repo_api_handler=GithubRequestHandler()
    )),
]
