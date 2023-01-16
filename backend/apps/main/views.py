import json

from django.http import HttpResponse
from django.shortcuts import render
from .services.jenkins_service import JenkinsService
from .services.gitlab_service import GitlabService
from rest_framework.views import APIView


# Create your views here.


class Main(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UserCreate(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("user create get api")

    def post(self, request, *args, **kwargs):
        '''
        1. 유저를 DB에 생성, 저장(가정)
        2. Gitlab 그룹 생성
        3. Jenkins folder 생성
        '''
        name = request.data.get('name')
        return JenkinsService().create_group(name)


class AppCreate(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("app create get api")

    def post(self, request, *args, **kwargs):
        '''
        1. Gitlab 프로젝트 생성
        2. Jenkins job 생성
        '''
        return HttpResponse("app create post api")


class Build(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("build get api")

    def post(self, request, *args, **kwargs):
        return HttpResponse("build post api")
