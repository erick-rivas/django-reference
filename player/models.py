from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=256)
    photo_url = models.CharField(max_length=512)