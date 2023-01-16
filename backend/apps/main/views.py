from django.shortcuts import render
from services import jenkins_service
from services import gitlab_service
# Create your views here.

def main(request):

    return rendser(request, 'index.html')
