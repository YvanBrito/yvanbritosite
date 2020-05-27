from django.db import models

class Dev(models.Model):
    name = models.CharField(max_length=100)
    github_username = models.CharField(max_length=30)
    bio = models.CharField(max_length=300, blank=True)
    avatar_url = models.CharField(max_length=100)
    techs = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
