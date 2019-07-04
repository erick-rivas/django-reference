"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from django.contrib import admin
from models.stats.match import Match
from models.player import Player
from models.stats.score import Score
from models.team import Team
from models.user import User
from models.helpers.file import File

class _Admin:  #

    @staticmethod
    def register():
        admin.site.register(File)
        admin.site.register(Match)
        admin.site.register(Player)
        admin.site.register(Score)
        admin.site.register(Team)
        admin.site.register(User)
