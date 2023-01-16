import json

import requests


class GitlabService:
    _GITLAB_TOKEN = "glpat-QzpN5tzKzEf2wqFXkKNG"
    _GITLAB_URL = "http://gitlab-service.default.svc"
    _BASE_TEMPLATE = {
        "SPRING": 2,
    }

    def create_user(self, user_name, email, password):
        header = f'Content-Type: application/json, PRIVATE_TOKEN: {self._GITLAB_TOKEN}'
        data = {"name": user_name, "user_name": user_name, "email": email, "password": password}
        url = f'{self._GITLAB_URL}/users'

        requests.post(url, headers=header, data=json.dumps(data))

    def create_group(self, user_name):
        header = f'Content-Type: application/json, PRIVATE_TOKEN: {self._GITLAB_TOKEN}'
        data = {"name": user_name, "path": user_name}
        url = f'{self._GITLAB_URL}/api/v4/groups'

        requests.post(url, headers=header, data=json.dumps(data))

    def create_project(self, namespace, app_name, base_template):
        header = f'Content-Type: application/json, PRIVATE_TOKEN: {self._GITLAB_TOKEN}'
        data = {"namespace": namespace, "name": app_name}
        url = f'{self._GITLAB_URL}/api/v4/projects/{self._BASE_TEMPLATE[base_template]}/fork'

        requests.post(url, headers=header, data=json.dumps(data))


if __name__ == '__main__':
    GitlabService().create_user("jaebom", "a.a", "www")
