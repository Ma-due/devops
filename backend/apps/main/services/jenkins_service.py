import requests
import xml.etree.ElementTree as ET
from .value import Jenkins, Gitlab


class JenkinsService:
    def create_folder(self, name):
        header = {'Content-Type': 'text/xml'}
        read = open('/Users/parkchangheon/my/git/devops/backend/apps/main/source/folder_template.xml') \
            .read()
        url = f'{Jenkins.URL.value}/createItem?name={name}'

        post = requests.post(url, headers=header, data=read, auth=Jenkins.TOKEN.value)
        return post.text

    def create_job(self, name, app_name):
        root = ET.parse('/Users/parkchangheon/my/git/devops/backend/apps/main/source/job_template.xml') \
            .getroot()
        url_tag = root.find('.//url')
        url_tag.text = f'{Gitlab.URL.value}/{name}/{app_name}.git'
        data = ET.tostring(root, encoding='utf8')

        header = {'Content-Type': 'text/xml'}
        url = f'{Jenkins.URL.value}/job/{name}/createItem?name={app_name}'
        post = requests.post(url, headers=header, data=data, auth=Jenkins.TOKEN.value)

        return post.status_code, post.text
