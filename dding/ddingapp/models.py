from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Gongmo(models.Model):
    title = models.CharField(max_length=50)

class Team(models.Model):
    name = models.CharField(max_length=50)
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gongmo = models.ForeignKey(Gongmo, on_delete=models.CASCADE)