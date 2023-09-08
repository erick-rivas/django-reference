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
            class Meta:
                model = Match
                fields = (
                    'id',
                    'date',
                    'type',
                    'local',
                    'visitor',
                )
        @admin.register(Match)
        class MatchAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = MatchResource
            fields = (
                'id',
                'created_at',
                'date',
                'type',
                'local',
                'visitor',
            )

            list_select_related = True
            list_display = ("id", "_name", "created_at")
            list_filter = ("id", "created_at")
            list_display_links = ("id", "_name",)
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
            )

            @admin.display(description="created_at")
            def created_at(self, instance):
                return instance.created_at

            def _name(self, obj):
                return str(obj)

            class Meta:
                model = Match
        
        class PlayerResource(resources.ModelResource):
            class Meta:
                model = Player
                fields = (
                    'id',
                    'name',
                    'photo',
                    'is_active',
                    'salary',
                    'team',
                    'position',
                )
        @admin.register(Player)
        class PlayerAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = PlayerResource
            fields = (
                'id',
                'created_at',
                'name',
                'photo',
                'is_active',
                'team',
                'position',
            )

            list_select_related = True
            list_display = ("id", "_name", "created_at")
            list_filter = ("id", "created_at")
            list_display_links = ("id", "_name",)
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
            )

            @admin.display(description="created_at")
            def created_at(self, instance):
                return instance.created_at

            def _name(self, obj):
                return str(obj)

            class Meta:
                model = Player
        
        class PlayerPositionResource(resources.ModelResource):
            class Meta:
                model = PlayerPosition
                fields = (
                    'id',
                    'name',
                    'details',
                )
        @admin.register(PlayerPosition)
        class PlayerPositionAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = PlayerPositionResource
            fields = (
                'id',
                'created_at',
                'name',
                'details',
            )

            list_select_related = True
            list_display = ("id", "_name", "created_at")
            list_filter = ("id", "created_at")
            list_display_links = ("id", "_name",)
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
            )

            @admin.display(description="created_at")
            def created_at(self, instance):
                return instance.created_at

            def _name(self, obj):
                return str(obj)

            class Meta:
                model = PlayerPosition
        
        class ScoreResource(resources.ModelResource):
            class Meta:
                model = Score
                fields = (
                    'id',
                    'min',
                    'player',
                    'match',
                )
        @admin.register(Score)
        class ScoreAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = ScoreResource
            fields = (
                'id',
                'created_at',
                'min',
                'player',
                'match',
            )

            list_select_related = True
            list_display = ("id", "_name", "created_at")
            list_filter = ("id", "created_at")
            list_display_links = ("id", "_name",)
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
            )

            @admin.display(description="created_at")
            def created_at(self, instance):
                return instance.created_at

            def _name(self, obj):
                return str(obj)

            class Meta:
                model = Score
        
        class TeamResource(resources.ModelResource):
            class Meta:
                model = Team
                fields = (
                    'id',
                    'name',
                    'logo',
                    'description',
                    'market_value',
                    'rival',
                )
        @admin.register(Team)
        class TeamAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = TeamResource
            fields = (
                'id',
                'created_at',
                'name',
                'logo',
                'description',
                'market_value',
                'identity_docs',
                'rival',
            )

            list_select_related = True
            list_display = ("id", "_name", "created_at")
            list_filter = ("id", "created_at")
            list_display_links = ("id", "_name",)
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
                'identity_docs',
            )

            @admin.display(description="created_at")
            def created_at(self, instance):
                return instance.created_at

            def _name(self, obj):
                return str(obj)

            class Meta:
                model = Team
        
        class UserResource(resources.ModelResource):
            class Meta:
                model = User
                fields = (
                    'id',
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'is_active',
                    'profile_image',
                    'teams',
                )
        from django.contrib.auth.admin import UserAdmin as UserAdminRoot
        @admin.register(User)
        class UserAdmin(UserAdminRoot, DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = UserResource
            fieldsets = [(None, {"fields": (
                'id',
                'created_at',
                'last_login',
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
                'is_staff',
                'is_active',
                'profile_image',
            )})]

            add_fieldsets = [(None, {"classes": ("wide",), "fields": (
                'username',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'email',
                'is_staff',
                'is_active',
                'profile_image',
            )})]

            list_display = ("id", "username", "first_name", "last_name", "last_login")
            list_filter = ("id", "username", "first_name", "last_name", "last_login")
            list_display_links = ("id", "username",)
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
                'last_login',
            )

            @admin.display(description="created_at")
            def created_at(self, instance):
                return instance.created_at

            def _name(self, obj):
                return str(obj)

            class Meta:
                model = User
        
        class FileResource(resources.ModelResource):
            class Meta:
                model = File
                fields = (
                    'id',
                    'name',
                    'url',
                    'size',
                )
        @admin.register(File)
        class FileAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = FileResource
            fields = (
                'id',
                'created_at',
                'name',
                'url',
                'size',
            )

            list_select_related = True
            list_display = ("id", "name", "url", "size")
            list_filter = ("id", "name", "url", "size")
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
            )

            @admin.display(description="created_at")
            def created_at(self, instance):
                return instance.created_at

            def _name(self, obj):
                return str(obj)

            class Meta:
                model = File