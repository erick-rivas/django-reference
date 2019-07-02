import os
from datetime import datetime
from django.db import models
from models.helpers.model import Model

class File(Model):  #

    url = models.URLField()
    size = models.IntegerField()
    name = models.CharField(max_length=128)