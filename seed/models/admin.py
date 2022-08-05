"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.models import Match
from app.models import Player
from app.models import PlayerPosition
from app.models import Score
from app.models import Team
from app.models import User
from app.models import File

class Admin:
    # pylint: disable=R0914,R0915
    @staticmethod
    def register():
        
        class MatchResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = Match
                fields = (
                    'id',
                    'created_at',
                    'date',
                    'type',
                    'local',
                    'visitor',
                    'scores',
                )

        class MatchAdmin(ImportExportModelAdmin):
            resource_class = MatchResource
        
        class PlayerResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = Player
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'photo',
                    'is_active',
                    'photo',
                    'team',
                    'position',
                )

        class PlayerAdmin(ImportExportModelAdmin):
            resource_class = PlayerResource
        
        class PlayerPositionResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = PlayerPosition
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'details',
                )

        class PlayerPositionAdmin(ImportExportModelAdmin):
            resource_class = PlayerPositionResource
        
        class ScoreResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = Score
                fields = (
                    'id',
                    'created_at',
                    'min',
                    'player',
                    'match',
                )

        class ScoreAdmin(ImportExportModelAdmin):
            resource_class = ScoreResource
        
        class TeamResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = Team
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'logo',
                    'description',
                    'market_value',
                    'identity_docs',
                    'logo',
                    'identity_docs',
                    'rival',
                    'players',
                )

        class TeamAdmin(ImportExportModelAdmin):
            resource_class = TeamResource
        
        class UserResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = User
                fields = (
                    'id',
                    'created_at',
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'is_active',
                    'profile_image',
                    'profile_image',
                    'teams',
                )

        class UserAdmin(ImportExportModelAdmin):
            resource_class = UserResource
        
        class FileResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = File
        class FileAdmin(ImportExportModelAdmin):
            resource_class = FileResource
        admin.site.register(Match, MatchAdmin)
        admin.site.register(Player, PlayerAdmin)
        admin.site.register(PlayerPosition, PlayerPositionAdmin)
        admin.site.register(Score, ScoreAdmin)
        admin.site.register(Team, TeamAdmin)
        admin.site.register(User, UserAdmin)
        admin.site.register(File, FileAdmin)