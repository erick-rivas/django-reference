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

    remove_orphan_files()

    if dir_path is None: dir_path = settings.MEDIA_ROOT
    if not os.path.exists(dir_path): return [], 0

    file_names = os.listdir(dir_path)
    num_original_files = len(file_names)
    removed_files = []
    print("====")
    print(f"Removing {dir_path} files...")
    for idx, file_name in enumerate(file_names):
        if idx % 1000 == 0:
            print(f"{idx} / {len(file_names)}")
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
                removed_files.append(file_path)

    return removed_files, num_original_files

def remove_orphan_files():
    from app.models import File
    file_fields = File._meta.get_fields()
    files = File.objects.all()

    rel_names = []
    for field in file_fields:
        typ = field.__class__.__name__
        if typ in ["ManyToOneRel", "ManyToManyRel"]:
            rel_names.append(field.name)

    print("====")
    print("Removing orphan files...")
    for idx, file in enumerate(files):
        if idx % 1000 == 0:
            print(f"{idx} / {len(files)}")
        is_orphan = True
        for rel_name in rel_names:
            if not is_orphan: continue
            rel_fields_count = len(getattr(file, rel_name).all())
            if rel_fields_count > 0:
                is_orphan = False
        if is_orphan:
            file.delete()