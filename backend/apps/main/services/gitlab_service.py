import json
from .value import Gitlab

import requests


class GitlabService:

    def create_user(self, name, email, password):
        header = {"Content-Type": "application/json", "PRIVATE_TOKEN": Gitlab.TOKEN.value}
        data = {"name": name, "user_name": name, "email": email, "password": password,
                "skip_confirmation": True}
        url = f'{Gitlab.URL.value}/api/v4/users'

        post = requests.post(url, headers=header, data=json.dumps(data))
        print(post.json())

    def create_project(self, namespace, app_name, kind):
        header = f'Content-Type: application/json, PRIVATE_TOKEN: {Gitlab.TOKEN.value}'
        data = {"namespace_id": namespace, "name": app_name, "path": app_name}
        url = f'{Gitlab.URL.value}/api/v4/projects/{Gitlab.KIND.value[kind]}/fork'

        post = requests.post(url, headers=header, data=json.dumps(data))
        return post.status_code, post.text
