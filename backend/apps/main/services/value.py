from enum import Enum


class Gitlab(Enum):
    URL = "http://gitlab-service.default.svc"
    KIND = {
        'spring': 2,
    }
    TOKEN = "glpat-QzpN5tzKzEf2wqFXkKNG"


class Jenkins(Enum):
    URL = "http://jenkins-service.jenkins.svc:8080"
    # URL = "http://34.168.30.192:31361"
    TOKEN = ("root", "11d0ffe0740df9240b1ba4a6918733ed5f")