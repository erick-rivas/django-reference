from datetime import datetime
from django.db import models
from models.helpers.model import Model

class File(Model):  #

    file = models.FileField()

    @property
    def url(self):
        return self.file.url

    @property
    def size(self):
        return self.file.size

    @property
    def name(self):
        return self.file.name
