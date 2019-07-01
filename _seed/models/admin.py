"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from django.contrib import admin
from models.user import User
from models.team import Team
from models.player import Player
from models.match import Match
from models.score import Score
from models.helpers.file import File

class _Admin:  #

    @staticmethod
    def register():
        admin.site.register(File)
        admin.site.register(User)
        admin.site.register(Team)
        admin.site.register(Player)
        admin.site.register(Match)
        admin.site.register(Score)
