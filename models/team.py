from django.db import models

from models.helpers.model import Model

class Team(Model):
    name = models.CharField(max_length=256)
    logo_url = models.CharField(max_length=512)

    def __str__(self):
        return self.to_str(self.name)