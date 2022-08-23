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
        
        class MatchResource(resources.ModelResource):
            pass

        class MatchAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = MatchResource
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
        
        class PlayerResource(resources.ModelResource):
            pass

        class PlayerAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = PlayerResource
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
        
        class PlayerPositionResource(resources.ModelResource):
            pass

        class PlayerPositionAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = PlayerPositionResource
            class Meta:
                model = PlayerPosition
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'details',
                )
        
        class ScoreResource(resources.ModelResource):
            pass

        class ScoreAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = ScoreResource
            class Meta:
                model = Score
                fields = (
                    'id',
                    'created_at',
                    'min',
                    'player',
                    'match',
                )
        
        class TeamResource(resources.ModelResource):
            pass

        class TeamAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = TeamResource
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
        
        class UserResource(resources.ModelResource):
            pass

        class UserAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = UserResource
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
        
        class FileResource(resources.ModelResource):
            pass

        class FileAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = FileResource
            class Meta:
                model = File
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'url',
                    'size'
                )
        admin.site.register(Match, MatchAdmin)
        admin.site.register(Player, PlayerAdmin)
        admin.site.register(PlayerPosition, PlayerPositionAdmin)
        admin.site.register(Score, ScoreAdmin)
        admin.site.register(Team, TeamAdmin)
        admin.site.register(User, UserAdmin)
        admin.site.register(File, FileAdmin)