from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class RepoDetails(APIView):

    renderer_classes = [JSONRenderer]
    repo_api_handler = None

    def get(self, request, owner=None, repository=None):
        if owner is None or repository is None:
            return Response({"You must provide user and repository name"})
        response = self.repo_api_handler(owner, repository)
        return Response({"repository_details": response})


class RepoOwnerDetails(APIView):

    renderer_classes = [JSONRenderer]
    repo_api_handler = None

    def get(self, request, owner=None, repository=None):
        if owner is None or repository is None:
            return Response({"You must provide user and repository name"})
        response = self.repo_api_handler.fetch_owner(owner, repository)
        return Response({"repository_owner_details": response})


class RepoCommitsDetails(APIView):

    renderer_classes = [JSONRenderer]
    repo_api_handler = None

    def get(self, request, owner=None, repository=None):
        if owner is None or repository is None:
            return Response({"You must provide user and repository name"})
        response = self.repo_api_handler.fetch_commits(owner, repository)
        return Response({"repository_commits_details": response})
