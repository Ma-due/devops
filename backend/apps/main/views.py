import json

from django.http import HttpResponse
from django.shortcuts import render
from .services.jenkins_service import JenkinsService
from .services.gitlab_service import GitlabService
from .services.argocd_service import ArgocdService
from rest_framework.views import APIView

# Create your views here.
JENKINS = JenkinsService()
GITLAB = GitlabService()
ARGOCD = ArgocdService()


class Main(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class User(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("user create get api")

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        passwd = request.data.get('password')
        email = request.data.get('email')

        folder = JENKINS.create_folder(name)
        gitlab_create_user = GITLAB.create_user(name, email, passwd)

        return HttpResponse(200, folder + gitlab_create_user)


class App(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("app create get api")

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        app_name = request.data.get('app_name')
        kind = request.data.get('kind')

        JENKINS.create_job(name, app_name)
        namespace_id = GITLAB.get_user_namespace_id(name)
        GITLAB.create_project(namespace_id, app_name, kind)

        return HttpResponse("app create post api")


class Build(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("build get api")

    def post(self, request, *args, **kwargs):
        user_name = request.data.get('name')
        app_name = request.data.get('app_name')

        job = JENKINS.build_job(user_name, app_name)

        return job


class Deploy(APIView):
    def post(self, request, *args, **kwargs):
        user_name = request.data.get('name')
        app_name = request.data.get('app_name')

        build_number = JENKINS.build_number(user_name, app_name)
        create_app = ARGOCD.create_app(user_name, app_name, build_number)

        return create_app
