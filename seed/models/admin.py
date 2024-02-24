"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django import forms
from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from seed.models.helpers.code_widget import CodeWidget
from seed.models.helpers.json_widget import JsonWidget
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
        class MatchForm(forms.ModelForm):
            model = Match
            class Meta:
                fields = '__all__'
                widgets = {
                }
        @admin.register(Match)
        class MatchAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = MatchResource
            form = MatchForm
            fields = (
                'id',
                'created_at',
                'date',
                'type',
                'local',
                'visitor',
            )

            list_select_related = True
            list_display = ('id', '_name', 'created_at')
            list_display_links = ('id', '_name',)
            list_filter = (
                'created_at',
                'date',
                'type',
            )
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
            )

            autocomplete_fields = (
                'local',
                'visitor',
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
        class PlayerForm(forms.ModelForm):
            model = Player
            class Meta:
                fields = '__all__'
                widgets = {
                }
        @admin.register(Player)
        class PlayerAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = PlayerResource
            form = PlayerForm
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
            list_display = ('id', '_name', 'created_at')
            list_display_links = ('id', '_name',)
            list_filter = (
                'created_at',
                'is_active',
            )
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
            )

            autocomplete_fields = (
                'photo',
                'team',
                'position',
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
                    'code',
                    'stats',
                    'details',
                )
        class PlayerPositionForm(forms.ModelForm):
            model = PlayerPosition
            class Meta:
                fields = '__all__'
                widgets = {
                    'code': CodeWidget(),
                    'stats': JsonWidget(),
                    'details': JsonWidget(),
                }
        @admin.register(PlayerPosition)
        class PlayerPositionAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = PlayerPositionResource
            form = PlayerPositionForm
            fields = (
                'id',
                'created_at',
                'name',
                'code',
                'stats',
                'details',
            )

            list_select_related = True
            list_display = ('id', '_name', 'created_at')
            list_display_links = ('id', '_name',)
            list_filter = (
                'created_at',
            )
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
            )

            autocomplete_fields = (
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
        class ScoreForm(forms.ModelForm):
            model = Score
            class Meta:
                fields = '__all__'
                widgets = {
                }
        @admin.register(Score)
        class ScoreAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = ScoreResource
            form = ScoreForm
            fields = (
                'id',
                'created_at',
                'min',
                'player',
                'match',
            )

            list_select_related = True
            list_display = ('id', '_name', 'created_at')
            list_display_links = ('id', '_name',)
            list_filter = (
                'created_at',
            )
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
            )

            autocomplete_fields = (
                'player',
                'match',
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
        class TeamForm(forms.ModelForm):
            model = Team
            class Meta:
                fields = '__all__'
                widgets = {
                }
        @admin.register(Team)
        class TeamAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = TeamResource
            form = TeamForm
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
            list_display = ('id', '_name', 'created_at')
            list_display_links = ('id', '_name',)
            list_filter = (
                'created_at',
            )
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
                'identity_docs',
            )

            autocomplete_fields = (
                'logo',
                'rival',
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
        class UserForm(forms.ModelForm):
            model = User
            class Meta:
                fields = '__all__'
                widgets = {
                }
        from django.contrib.auth.admin import UserAdmin as UserAdminRoot
        @admin.register(User)
        class UserAdmin(UserAdminRoot, DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = UserResource
            form = UserForm
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
                'teams',
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
                'teams',
            )})]

            list_display = ('id', 'username', 'first_name', 'last_name', 'last_login')
            list_display_links = ('id', 'username',)
            list_filter = (
                'created_at',
                'is_staff',
                'is_active',

            )
            ordering = ("-created_at",)

            readonly_fields = (
                'id',
                'created_at',
                'last_login',
            )

            autocomplete_fields = (
                'profile_image',
                'teams',
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
            list_filter = ("created_at", "size")
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