import json

from django.http import HttpResponse

from .value import Argocd, Gitlab
import requests


class ArgocdService:
    def get_app(self):
        url = f'{Argocd.URL.value}/api/v1/applications'
        header = {"Authorization": f'Bearer {Argocd.TOKEN.value}'}
        get = requests.get(url, headers=header)

        return HttpResponse(get.status_code, get.text)

    def create_app(self, user_name, app_name, build_number):
        url = f'{Argocd.URL.value}/api/v1/applications'
        headers = {"Content-Type": "application/json",
                   "Authorization": f'Bearer {Argocd.TOKEN.value}'}

        data = json.load(open(Argocd.APP.value, 'r'))
        data["metadata"]["name"] = f'{user_name}-{app_name}'
        data["spec"]["destination"]["namespace"] = user_name
        repo_url = f'{Gitlab.URL.value}/{user_name}/{app_name}.git'
        data["spec"]["source"]["repoURL"] = repo_url
        data["spec"]["source"]["helm"]["parameters"][0]["value"] = user_name
        data["spec"]["source"]["helm"]["parameters"][1]["value"] = app_name
        data["spec"]["source"]["helm"]["parameters"][2]["value"] = build_number

        post = requests.post(url, data=json.dumps(data), headers=headers)
        return HttpResponse(post.status_code, post.text)

    def app_sync(self, app_name):
        url = f'{Argocd.URL.value}/api/v1/applications/{app_name}/sync'
        headers = {"Authorization": f'Bearer {Argocd.TOKEN.value}'}

        post = requests.post(url, headers=headers)
        return HttpResponse(post.status_code, post.text)
