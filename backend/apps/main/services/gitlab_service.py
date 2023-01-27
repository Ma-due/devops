import json
from .value import Gitlab

import requests


class GitlabService:
    def get_user_namespace_id(self, name):
        header = {"PRIVATE-TOKEN": Gitlab.TOKEN.value}
        url = f'{Gitlab.URL2.value}/api/v4/users?search={name}'
        get = requests.get(url, headers=header)

        return get.json()[0]['namespace_id']

    def create_user(self, name, email, password):
        header = {"Content-Type": "application/json", "PRIVATE-TOKEN": Gitlab.TOKEN.value}
        data = {"name": name, "username": name, "email": email, "password": password,
                "skip_confirmation": True}
        url = f'{Gitlab.URL2.value}/api/v4/users'

        post = requests.post(url, headers=header, data=json.dumps(data))
        return post.text

    def create_project(self, namespace, app_name, kind):
        header = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': Gitlab.TOKEN.value}
        data = {"namespace_id": namespace, "name": app_name, "path": app_name}
        url = f'{Gitlab.URL2.value}/api/v4/projects/{Gitlab.KIND.value[kind]}/fork'

        post = requests.post(url, headers=header, data=json.dumps(data))

        return post.status_code, post.text
