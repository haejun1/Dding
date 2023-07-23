from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Gongmo(models.Model):
    title = models.CharField(max_length=50)

class Jickgoon(models.Model):
    name = models.CharField(max_length=50)

class Team(models.Model):
    name = models.CharField(max_length=50)
    gongmo = models.ForeignKey(Gongmo, on_delete=models.CASCADE)
    jickgoons = models.ManyToManyField(Jickgoon, through="Member")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    jickgoon = models.ForeignKey(Jickgoon, on_delete=models.CASCADE)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    jickgoon = models.ForeignKey('Jickgoon', on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    message = models.TextField(null=True) 