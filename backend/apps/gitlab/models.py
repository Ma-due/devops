from django.db import models
from ..main.models import User


# Create your models here.
class GitlabUser(models.Model):
    user_name = models.TextField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class GitlabProject(models.Model):
    name = models.TextField(max_length=20)
    user_id = models.ForeignKey(GitlabUser, on_delete=models.DO_NOTHING)