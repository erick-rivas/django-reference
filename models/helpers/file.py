import os
from datetime import datetime
from django.db import models
from models.helpers.model import Model

class File(Model):  #

    file = models.FileField()

    @property
    def url(self):
        host_url = os.getenv('HOST_URL')
        url = self.file.url
        return url if url.startswith("http") else host_url + url

    @property
    def size(self):
        return self.file.size

    @property
    def name(self):
        return self.file.name
