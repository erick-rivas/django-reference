"""
__Seed builder__
  (Read_only) Domain helper
"""

import os
from datetime import datetime

from django.conf import settings

def clean_files(dir_path=None, min_file_age=72):
    """
    Removes files without a related File object

    :param path: Path of the file folder (default: Media path)
    :param min_file_age: Min file age to remove in hours
    """
    from app.models import File

    if dir_path is None: dir_path = settings.MEDIA_ROOT
    if not os.path.exists(dir_path): return

    file_names = os.listdir(dir_path)
    for file_name in file_names:

        file_path = os.path.join(dir_path, file_name)
        if not os.path.isfile(file_path): continue

        if not File.objects.filter(name=file_name).exists():
            timestamp = os.path.getctime(file_path)
            created_at = datetime.fromtimestamp(timestamp)

            difference = datetime.now() - created_at
            seconds = difference.total_seconds()
            minutes = seconds / 60
            hours = minutes / 60
            if hours > min_file_age:
                os.remove(file_path)