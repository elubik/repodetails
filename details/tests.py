from unittest import mock

from django.test import TestCase, Client

from details.views import RepoOwnerDetails, RepoDetails, RepoCommitsDetails
from repository.github_request_handler import GithubRequestHandler, \
    RepositoryInterface


def mocked_requests_repo_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({"repository_details": {
        "compare_url": "https://api.github.com/repos/pawel26/worker/compare/{base}...{head}",
        "open_issues": 0,
        "url": "https://api.github.com/repos/pawel26/worker",
        "watchers": 0,
        "has_wiki": True,
        "downloads_url": "https://api.github.com/repos/pawel26/worker/downloads",
        "labels_url": "https://api.github.com/repos/pawel26/worker/labels{/name}",
        "tags_url": "https://api.github.com/repos/pawel26/worker/tags",
        "created_at": "2016-02-18T19:54:48Z",
        "hooks_url": "https://api.github.com/repos/pawel26/worker/hooks",
        "issue_comment_url": "https://api.github.com/repos/pawel26/worker/issues/comments{/number}",
        "commits_url": "https://api.github.com/repos/pawel26/worker/commits{/sha}",
        "keys_url": "https://api.github.com/repos/pawel26/worker/keys{/key_id}",
        "description": None,
        "homepage": None,
        "git_commits_url": "https://api.github.com/repos/pawel26/worker/git/commits{/sha}",
        "mirror_url": None,
        "has_downloads": None,
        "blobs_url": "https://api.github.com/repos/pawel26/worker/git/blobs{/sha}",
        "subscribers_url": "https://api.github.com/repos/pawel26/worker/subscribers",
        "network_count": 2,
        "pushed_at": "2016-02-26T17:28:12Z",
        "full_name": "pawel26/worker",
        "milestones_url": "https://api.github.com/repos/pawel26/worker/milestones{/number}",
        "forks_url": "https://api.github.com/repos/pawel26/worker/forks",
        "git_refs_url": "https://api.github.com/repos/pawel26/worker/git/refs{/sha}",
        "name": "worker",
        "forks": 2,
        "releases_url": "https://api.github.com/repos/pawel26/worker/releases{/id}",
        "stargazers_count": 0,
        "has_projects": True,
        "contributors_url": "https://api.github.com/repos/pawel26/worker/contributors",
        "private": False,
        "size": 4,
        "notifications_url": "https://api.github.com/repos/pawel26/worker/notifications{?since,all,participating}",
        "has_pages": False,
        "trees_url": "https://api.github.com/repos/pawel26/worker/git/trees{/sha}",
        "pulls_url": "https://api.github.com/repos/pawel26/worker/pulls{/number}",
        "svn_url": "https://github.com/pawel26/worker",
        "assignees_url": "https://api.github.com/repos/pawel26/worker/assignees{/user}",
        "teams_url": "https://api.github.com/repos/pawel26/worker/teams",
        "html_url": "https://github.com/pawel26/worker",
        "watchers_count": 0,
        "collaborators_url": "https://api.github.com/repos/pawel26/worker/collaborators{/collaborator}",
        "fork": False,
        "contents_url": "https://api.github.com/repos/pawel26/worker/contents/{+path}",
        "issue_events_url": "https://api.github.com/repos/pawel26/worker/issues/events{/number}",
        "comments_url": "https://api.github.com/repos/pawel26/worker/comments{/number}",
        "language": "JavaScript",
        "archive_url": "https://api.github.com/repos/pawel26/worker/{archive_format}{/ref}",
        "subscribers_count": 1,
        "git_tags_url": "https://api.github.com/repos/pawel26/worker/git/tags{/sha}",
        "clone_url": "https://github.com/pawel26/worker.git",
        "forks_count": 2,
        "license": None,
        "temp_clone_token": None,
        "deployments_url": "https://api.github.com/repos/pawel26/worker/deployments",
        "branches_url": "https://api.github.com/repos/pawel26/worker/branches{/branch}",
        "merges_url": "https://api.github.com/repos/pawel26/worker/merges",
        "ssh_url": "git@github.com:pawel26/worker.git",
        "id": 52034401,
        "git_url": "git://github.com/pawel26/worker.git",
        "subscription_url": "https://api.github.com/repos/pawel26/worker/subscription",
        "events_url": "https://api.github.com/repos/pawel26/worker/events",
        "archived": False,
        "owner": {
            "organizations_url": "https://api.github.com/users/pawel26/orgs",
            "url": "https://api.github.com/users/pawel26",
            "html_url": "https://github.com/pawel26",
            "gravatar_id": "",
            "id": 6375401,
            "starred_url": "https://api.github.com/users/pawel26/starred{/owner}{/repo}",
            "events_url": "https://api.github.com/users/pawel26/events{/privacy}",
            "received_events_url": "https://api.github.com/users/pawel26/received_events",
            "followers_url": "https://api.github.com/users/pawel26/followers",
            "following_url": "https://api.github.com/users/pawel26/following{/other_user}",
            "login": "pawel26",
            "node_id": "MDQ6VXNlcjYzNzU0MDE=",
            "type": "User",
            "avatar_url": "https://avatars1.githubusercontent.com/u/6375401?v=4",
            "subscriptions_url": "https://api.github.com/users/pawel26/subscriptions",
            "repos_url": "https://api.github.com/users/pawel26/repos",
            "gists_url": "https://api.github.com/users/pawel26/gists{/gist_id}",
            "site_admin": False
        },
        "node_id": "MDEwOlJlcG9zaXRvcnk1MjAzNDQwMQ==",
        "open_issues_count": 0,
        "issues_url": "https://api.github.com/repos/pawel26/worker/issues{/number}",
        "disabled": False,
        "languages_url": "https://api.github.com/repos/pawel26/worker/languages",
        "updated_at": "2016-02-18T19:55:36Z",
        "stargazers_url": "https://api.github.com/repos/pawel26/worker/stargazers",
        "default_branch": "master",
        "statuses_url": "https://api.github.com/repos/pawel26/worker/statuses/{sha}",
        "has_issues": True}}, 200)


def mocked_requests_owner_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({"owner": {
            "url": "https://api.github.com/users/pawel26",
            "followers_url": "https://api.github.com/users/pawel26/followers",
            "repos_url": "https://api.github.com/users/pawel26/repos",
            "login": "pawel26",
            "received_events_url": "https://api.github.com/users/pawel26/received_events",
            "organizations_url": "https://api.github.com/users/pawel26/orgs",
            "events_url": "https://api.github.com/users/pawel26/events{/privacy}",
            "type": "User",
            "html_url": "https://github.com/pawel26",
            "site_admin": False,
            "id": 6375401,
            "gists_url": "https://api.github.com/users/pawel26/gists{/gist_id}",
            "gravatar_id": "",
            "avatar_url": "https://avatars1.githubusercontent.com/u/6375401?v=4",
            "starred_url": "https://api.github.com/users/pawel26/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/pawel26/subscriptions",
            "following_url": "https://api.github.com/users/pawel26/following{/other_user}",
            "node_id": "MDQ6VXNlcjYzNzU0MDE="}}, 200)


def mocked_requests_repo_commits_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({
        "compare_url": "https://api.github.com/repos/pawel26/worker/compare/{base}...{head}",
        "open_issues": 0,
        "url": "https://api.github.com/repos/pawel26/worker",
        "watchers": 0,
        "has_wiki": True,
        "downloads_url": "https://api.github.com/repos/pawel26/worker/downloads",
        "labels_url": "https://api.github.com/repos/pawel26/worker/labels{/name}",
        "tags_url": "https://api.github.com/repos/pawel26/worker/tags",
        "created_at": "2016-02-18T19:54:48Z",
        "hooks_url": "https://api.github.com/repos/pawel26/worker/hooks",
        "issue_comment_url": "https://api.github.com/repos/pawel26/worker/issues/comments{/number}",
        "commits_url": "https://api.github.com/repos/pawel26/worker/commits{/sha}",
        "keys_url": "https://api.github.com/repos/pawel26/worker/keys{/key_id}",
        "description": None,
        "homepage": None,
        "git_commits_url": "https://api.github.com/repos/pawel26/worker/git/commits{/sha}",
        "mirror_url": None,
        "has_downloads": None,
        "blobs_url": "https://api.github.com/repos/pawel26/worker/git/blobs{/sha}",
        "subscribers_url": "https://api.github.com/repos/pawel26/worker/subscribers",
        "network_count": 2,
        "pushed_at": "2016-02-26T17:28:12Z",
        "full_name": "pawel26/worker",
        "milestones_url": "https://api.github.com/repos/pawel26/worker/milestones{/number}",
        "forks_url": "https://api.github.com/repos/pawel26/worker/forks",
        "git_refs_url": "https://api.github.com/repos/pawel26/worker/git/refs{/sha}",
        "name": "worker",
        "forks": 2,
        "releases_url": "https://api.github.com/repos/pawel26/worker/releases{/id}",
        "stargazers_count": 0,
        "has_projects": True,
        "contributors_url": "https://api.github.com/repos/pawel26/worker/contributors",
        "private": False,
        "size": 4,
        "notifications_url": "https://api.github.com/repos/pawel26/worker/notifications{?since,all,participating}",
        "has_pages": False,
        "trees_url": "https://api.github.com/repos/pawel26/worker/git/trees{/sha}",
        "pulls_url": "https://api.github.com/repos/pawel26/worker/pulls{/number}",
        "svn_url": "https://github.com/pawel26/worker",
        "assignees_url": "https://api.github.com/repos/pawel26/worker/assignees{/user}",
        "teams_url": "https://api.github.com/repos/pawel26/worker/teams",
        "html_url": "https://github.com/pawel26/worker",
        "watchers_count": 0,
        "collaborators_url": "https://api.github.com/repos/pawel26/worker/collaborators{/collaborator}",
        "fork": False,
        "contents_url": "https://api.github.com/repos/pawel26/worker/contents/{+path}",
        "issue_events_url": "https://api.github.com/repos/pawel26/worker/issues/events{/number}",
        "comments_url": "https://api.github.com/repos/pawel26/worker/comments{/number}",
        "language": "JavaScript",
        "archive_url": "https://api.github.com/repos/pawel26/worker/{archive_format}{/ref}",
        "subscribers_count": 1,
        "git_tags_url": "https://api.github.com/repos/pawel26/worker/git/tags{/sha}",
        "clone_url": "https://github.com/pawel26/worker.git",
        "forks_count": 2,
        "license": None,
        "temp_clone_token": None,
        "deployments_url": "https://api.github.com/repos/pawel26/worker/deployments",
        "branches_url": "https://api.github.com/repos/pawel26/worker/branches{/branch}",
        "merges_url": "https://api.github.com/repos/pawel26/worker/merges",
        "ssh_url": "git@github.com:pawel26/worker.git",
        "id": 52034401,
        "git_url": "git://github.com/pawel26/worker.git",
        "subscription_url": "https://api.github.com/repos/pawel26/worker/subscription",
        "events_url": "https://api.github.com/repos/pawel26/worker/events",
        "archived": False,
        "owner": {
            "organizations_url": "https://api.github.com/users/pawel26/orgs",
            "url": "https://api.github.com/users/pawel26",
            "html_url": "https://github.com/pawel26",
            "gravatar_id": "",
            "id": 6375401,
            "starred_url": "https://api.github.com/users/pawel26/starred{/owner}{/repo}",
            "events_url": "https://api.github.com/users/pawel26/events{/privacy}",
            "received_events_url": "https://api.github.com/users/pawel26/received_events",
            "followers_url": "https://api.github.com/users/pawel26/followers",
            "following_url": "https://api.github.com/users/pawel26/following{/other_user}",
            "login": "pawel26",
            "node_id": "MDQ6VXNlcjYzNzU0MDE=",
            "type": "User",
            "avatar_url": "https://avatars1.githubusercontent.com/u/6375401?v=4",
            "subscriptions_url": "https://api.github.com/users/pawel26/subscriptions",
            "repos_url": "https://api.github.com/users/pawel26/repos",
            "gists_url": "https://api.github.com/users/pawel26/gists{/gist_id}",
            "site_admin": False
        },
        "node_id": "MDEwOlJlcG9zaXRvcnk1MjAzNDQwMQ==",
        "open_issues_count": 0,
        "issues_url": "https://api.github.com/repos/pawel26/worker/issues{/number}",
        "disabled": False,
        "languages_url": "https://api.github.com/repos/pawel26/worker/languages",
        "updated_at": "2016-02-18T19:55:36Z",
        "stargazers_url": "https://api.github.com/repos/pawel26/worker/stargazers",
        "default_branch": "master",
        "statuses_url": "https://api.github.com/repos/pawel26/worker/statuses/{sha}",
        "has_issues": True}, 200)


class GetRepoDetailsTest(TestCase):

    def setUp(self):
        req_handler = GithubRequestHandler()
        self.rd = RepoDetails()
        self.rd.repo_api_handler = req_handler
        self.client = Client()

    @mock.patch('repository.github_request_handler.requests.get',
                side_effect=mocked_requests_repo_get)
    def test_get_valid_owner_details_success(self, mock_get):
        response = self.rd.get('pawel26', 'worker')

        self.assertEqual(response.status_code, 200)

    @mock.patch.object(
        GithubRequestHandler, "make_api_call",
        lambda self, resource_link: {"repository_details": {}})
    def test_get_valid_owner_details(self):
        response = self.rd.get(None, 'pawel26', 'worker')

        assert "repository_details" in response.data

    def test_request_handler_is_set(self):
        assert self.rd.repo_api_handler


class GetRepoOwnerDetailsTest(TestCase):

    def setUp(self):
        self.rod = RepoOwnerDetails()
        req_handler = GithubRequestHandler()
        self.rod.repo_api_handler = req_handler
        self.client = Client()

    @mock.patch('repository.github_request_handler.requests.get',
                side_effect=mocked_requests_owner_get)
    def test_get_valid_owner_details_success(self, mock_get):
        response = self.rod.get(None, 'pawel26', 'worker')

        self.assertEqual(response.status_code, 200)

    @mock.patch.object(GithubRequestHandler, "make_api_call",
                       lambda self, resource_link: {"owner": {}})
    def test_get_valid_owner_details(self):
        response = self.rod.get(None, 'pawel26', 'worker')

        assert "repository_owner_details" in response.data

    def test_request_handler_is_set(self):
        assert self.rod.repo_api_handler


class GetRepoCommitsDetailsTest(TestCase):

    def setUp(self):
        self.rcd = RepoCommitsDetails()
        req_handler = GithubRequestHandler()
        self.rcd.repo_api_handler = req_handler
        self.client = Client()

    @mock.patch('repository.github_request_handler.requests.get',
                side_effect=mocked_requests_repo_commits_get)
    def test_get_valid_owner_details_success(self, mock_get):
        response = self.rcd.get(None, 'pawel26', 'worker')

        self.assertEqual(response.status_code, 200)

    @mock.patch.object(GithubRequestHandler, "make_api_call",
                       lambda self, resource_link: {"commits_url": "fake_http_link"})
    def test_get_valid_owner_details(self):
        response = self.rcd.get(None, 'pawel26', 'worker')

        assert "repository_commits_details" in response.data

    def test_request_handler_is_set(self):
        assert self.rcd.repo_api_handler


class GithubRequestHandlerTest(TestCase):

    def setUp(self):
        self.req_obj = GithubRequestHandler()

    def test_is_repo_interface_subclass(self):
        assert isinstance(self.req_obj, RepositoryInterface)

    def test_request_handler_is_callable(self):
        assert callable(self.req_obj)

    def test_build_repository_url(self):
        user = "test"
        repository = "repo"
        url = self.req_obj.build_repository_url(user, repository)

        self.assertEqual(url, "https://api.github.com/repos/test/repo")