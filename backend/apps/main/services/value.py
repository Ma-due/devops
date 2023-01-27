from enum import Enum


class Gitlab(Enum):
    # URL2 = "http://34.168.30.192:30100"

    URL = "http://gitlab-service.default.svc"
    KIND = {
        'spring': 2,
    }
    TOKEN = "glpat-QzpN5tzKzEf2wqFXkKNG"


class Jenkins(Enum):
    # URL = "http://34.168.30.192:31361"

    URL = "http://jenkins-service.jenkins.svc:8080"
    TOKEN = ("root", "11d0ffe0740df9240b1ba4a6918733ed5f")


class XMLPath(Enum):
    # FOLDER = '/Users/parkchangheon/my/git/devops/backend/apps/main/source/folder_template.xml'
    # JOB = '/Users/parkchangheon/my/git/devops/backend/apps/main/source/job_template.xml'

    FOLDER = '/root/backend/apps/main/source/folder_template.xml'
    JOB = '/root/backend/apps/main/source/job_template.xml'



class Argocd(Enum):
    # URL = "http://34.168.30.192:30133"
    # APP = '/Users/parkchangheon/my/git/devops/backend/apps/main/source/app.json'

    TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcmdvY2QiLCJzdWIiOiJhZG1pbjphcGlLZXkiLCJuYmYiOjE2NzQ3MjEzNTEsImlhdCI6MTY3NDcyMTM1MSwianRpIjoiYWNjYTM5M2ItM2VlOS00MTI1LWI2NzctZGQ5YmU2MzQ4NWNiIn0.MFIMM2wJ2mrsAHtfgAQD2g5s6JE4rxZpxEXqmY1r0wM"

    URL = "http://argocd-server.argocd.svc"
    APP = '/root/backend/apps/main/source/app.json'
