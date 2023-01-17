import json

from django.http import HttpResponse
from django.shortcuts import render
from .services.jenkins_service import JenkinsService
from .services.gitlab_service import GitlabService
from rest_framework.views import APIView


# Create your views here.
JENKINS = JenkinsService()
GITLAB = GitlabService()

class Main(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class User(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("user create get api")

    def post(self, request, *args, **kwargs):
        '''
        1. 유저를 DB에 생성, 저장(가정)
        2. Gitlab 그룹 생성
        3. Jenkins folder 생성
        '''
        name = request.data.get('name')
        passwd = request.data.get('password')
        email = request.data.get('email')

        JENKINS.create_folder(name)
        GITLAB.create_user(name, email, passwd)

        return HttpResponse("user create post api")


class App(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("app create get api")

    def post(self, request, *args, **kwargs):
        '''
        :param
        user name
        app name
        template
        1. Gitlab 프로젝트 생성
        2. Jenkins job 생성
        '''

        name = request.data.get('name')
        app_name = request.data.get('app_name')
        kind = request.data.get('kind')
        JENKINS.create_job(name, app_name, kind)
        #GITLAB.create_project(namespace_id, app_name, kind)

        return HttpResponse("app create post api")


class Build(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("build get api")

    def post(self, request, *args, **kwargs):
        return HttpResponse("build post api")
