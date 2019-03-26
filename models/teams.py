from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=256)
    logo_url = models.CharField(max_length=512)