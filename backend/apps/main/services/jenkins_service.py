import os

import requests


class JenkinsService:
    _JENKINS_URL = "http://jenkins-service.jenkins.svc"
    _JENKINS_TOKEN = ("root", "11d0ffe0740df9240b1ba4a6918733ed5f")

    def create_group(self, user_name):
        header = {'Content-Type:text/xml'}
        file = open('/root/devops/backend/main/source/folder_template.xml', 'rb')
        url = f'{self._JENKINS_URL}/createItem?name={user_name}'

        requests.post(url, headers=header, files=file, auth=self._JENKINS_TOKEN)

    def create_job(self, user_name, app_name):
        header = {'Content-Type:text/xml'}
        file = open('../source/job_template.xml', 'rb')
        url = f'{self._JENKINS_URL}/{user_name}/createItem?name={app_name}'

        requests.post(url, headers=header, files=file, auth=self._JENKINS_TOKEN)
