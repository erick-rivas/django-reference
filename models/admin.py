"""
__Seed builder__v1.0

  Guidelines: 
    - Include list_filter and search_fields if required
    - Reference filters: https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    - Reference search: https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
"""

from django.contrib import admin
from seed.helpers.model_admin import ModelAdminClass
from app.models import Player
from app.models import Team
from app.models import User
from app.models import Match
from app.models import Score
from app.models import File

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