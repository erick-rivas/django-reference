"""
__Seed builder__v0.1.8
  (Read_only) Builder helper
"""

import os
import uuid
from django.core.files.storage import default_storage
from urllib.parse import urlparse

from app.models import File

def save_file(f):
    filename = uuid.uuid4().hex + "_" + f.name
    name = default_storage.save(filename, f)
    size = default_storage.size(name)
    url = default_storage.url(name)
    host_url = os.getenv('HOST_URL')
    if url.startswith("http"):
        u = urlparse(url)
        url = u.scheme + "://" + u.netloc + u.path
    else:
        url = host_url + url
    return File.objects.create(name=name, size=size, url=url)