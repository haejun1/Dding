from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Gongmo(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    image = models.ImageField(null=True, upload_to="images/", blank=True)
    deadline = models.TextField()
    registration_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    leader = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    detail = models.TextField()
    gongmo = models.ForeignKey(Gongmo, on_delete=models.CASCADE)
    progress = models.TextField()
    registration_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)

class Jickgoon(models.Model):
    name = models.CharField(max_length=50)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Jickgoonjoin(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Jickgoon, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
