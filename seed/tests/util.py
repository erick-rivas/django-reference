"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.core.management import call_command
from django.db import connection

def fill_test_database():
    with connection.cursor() as cursor:
        cursor.execute('ALTER TABLE "_match" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "_player" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "_player_position" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "_score" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "_team" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "_user" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "file" DISABLE TRIGGER ALL;')
    call_command('loaddata', 'models/fixtures/.template.yaml', verbosity=0)