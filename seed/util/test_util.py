"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json
from django.core.management import call_command
from django.db import connection

def assert_json(json_a, json_b):
    """
    Compare the content of two json objects

    :param json_a: First json object
    :param json_b: Second json object
    :return: True if they are equal false otherwise
    """
    return \
        json.dumps(json_a, indent=2, sort_keys=True) == json.dumps(json_b, indent=2, sort_keys=True)

def fill_test_database():
    """
    Create a dump database filling with one registry of each model
    """
    with connection.cursor() as cursor:
        cursor.execute('ALTER TABLE "_match" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "_player" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "_player_position" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "_score" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "_team" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "_user" DISABLE TRIGGER ALL;')
        cursor.execute('ALTER TABLE "file" DISABLE TRIGGER ALL;')
    call_command('loaddata', 'seed/tests/fixtures.yaml', verbosity=0)