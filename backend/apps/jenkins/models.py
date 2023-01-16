from django.db import models
from ..main.models import User


# Create your models here.
class JenkinsFolder(models.Model):
    name = models.TextField(max_length=20)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class JenkinsJob(models.Model):
    name = models.TextField(max_length=20)
    folder = models.ForeignKey(JenkinsFolder, on_delete=models.DO_NOTHING)
