from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Gongmo(models.Model):
    title = models.CharField(max_length=50)

class Team(models.Model):
    name = models.CharField(max_length=50)
    gongmo = models.ForeignKey(Gongmo, on_delete=models.CASCADE)