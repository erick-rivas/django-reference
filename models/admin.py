"""
__Seed builder__v1.0

  Guidelines: 
    - Include list_filter and search_fields if required
    - Reference filters: https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    - Reference search: https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
"""

from django.contrib import admin
from sbuild.helpers.model_admin import ModelAdminClass
from models.helpers.file import File
from models.player import Player
from models.team import Team
from models.user import User
from models.stats.match import Match
from models.stats.score import Score

class FileAdmin(ModelAdminClass(File)):
    pass

class PlayerAdmin(ModelAdminClass(Player)):
    pass

class TeamAdmin(ModelAdminClass(Team)):
    pass

class UserAdmin(ModelAdminClass(User)):
    pass

class MatchAdmin(ModelAdminClass(Match)):
    pass

class ScoreAdmin(ModelAdminClass(Score)):
    pass

admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(File, FileAdmin)
