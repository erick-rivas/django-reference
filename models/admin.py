"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from django.contrib import admin
from _seed.models.admin import _Admin

_Admin().register()