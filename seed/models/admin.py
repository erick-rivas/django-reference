"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib import admin
from seed.helpers.model_admin import ModelAdminClass
from app.models import Match
from app.models import Player
from app.models import PlayerPosition
from app.models import Score
from app.models import Team
from app.models import User
from app.models import File

class _Admin:  #

  @staticmethod
  def register():  #
      
      class MatchAdmin(ModelAdminClass(Match)):
          pass
      
      class PlayerAdmin(ModelAdminClass(Player)):
          pass
      
      class PlayerPositionAdmin(ModelAdminClass(PlayerPosition)):
          pass
      
      class ScoreAdmin(ModelAdminClass(Score)):
          pass
      
      class TeamAdmin(ModelAdminClass(Team)):
          pass
      
      class UserAdmin(ModelAdminClass(User)):
          pass
      
      class FileAdmin(ModelAdminClass(File)):
          pass
      admin.site.register(Match, MatchAdmin)
      admin.site.register(Player, PlayerAdmin)
      admin.site.register(PlayerPosition, PlayerPositionAdmin)
      admin.site.register(Score, ScoreAdmin)
      admin.site.register(Team, TeamAdmin)
      admin.site.register(User, UserAdmin)
      admin.site.register(File, FileAdmin)
