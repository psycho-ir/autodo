from rest_framework.response import Response
from rest_framework.views import APIView
from .github import parse


class GithubHook(APIView):
    def post(self, request):
        print(request.body)
        print(request.data)
        parse(request)
        return Response("wow")
