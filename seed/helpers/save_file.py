"""
__Seed builder__v0.2.0
  (Read_only) Domain helper
"""

import os
import uuid
from django.core.files.storage import default_storage
from urllib.parse import urlparse
from app.models import File


def save_file(path, mode="rb"):
    """
   Saves a local file in media/static folder and in file model (database) based on server settings

   :param path: File path
   :param mode: File open mode (Default rb)
   :return: File model (app.models.File)
   """
    with open(path, mode=mode) as file:
        return save_file_obj(file)


def save_file_obj(file):
    """
    Saves a local file in media/static folder and in file model (database) based on server settings

    :param file: File object in r mode
    :return: File model (app.models.File)
    """
    filename = uuid.uuid4().hex + "_" + file.name
    name = default_storage.save(filename, file)
    size = default_storage.size(name)
    url = default_storage.url(name)
    host_url = os.getenv('SERVER_URL')
    if url.startswith("http"):
        url_parsed = urlparse(url)
        url = url_parsed.scheme + "://" + url_parsed.netloc + url_parsed.path
    else:
        url = host_url + url
    return File.objects.create(name=name, size=size, url=url)