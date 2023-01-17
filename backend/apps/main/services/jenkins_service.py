import requests
import xml.etree.ElementTree as ET
from .value import Jenkins, Gitlab


class JenkinsService:
    def get_main(self):
        get = requests.get(Jenkins.URL.value)
        return get

    def create_folder(self, user_name):
        header = {'Content-Type': 'text/xml'}
        read = open('/root/backend/apps/main/source/folder_template.xml') \
            .read()
        url = f'{Jenkins.URL}/createItem?name={user_name}'

        post = requests.post(url, headers=header, data=read, auth=Jenkins.TOKEN.value)
        return post.status_code, post.text

    def create_job(self, user_name, app_name, kind):
        root = ET.parse('/root/backend/apps/main/source/job_template.xml') \
            .getroot()
        url_tag = root.find('.//url')
        url_tag.text = f'{Gitlab.URL.value}/{user_name}/{app_name}'
        data = ET.tostring(root, encoding='utf8')

        header = {'Content-Type:text/xml'}
        url = f'{Jenkins.URL.value}/{user_name}/createItem?name={app_name}'
        post = requests.post(url, headers=header, data=data, auth=Jenkins.TOKEN.value)

        return post.status_code, post.text
