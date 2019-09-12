"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_match_viewset():
    from views.matches import MatchViewSet
    return MatchViewSet

def get_player_viewset():
    from views.players import PlayerViewSet
    return PlayerViewSet

def get_player_type_viewset():
    from views.player_types import PlayerTypeViewSet
    return PlayerTypeViewSet

def get_score_viewset():
    from views.scores import ScoreViewSet
    return ScoreViewSet

def get_team_viewset():
    from views.teams import TeamViewSet
    return TeamViewSet

def get_user_viewset():
    from views.users import UserViewSet
    return UserViewSet

def get_file_view():
    from seed.views.helpers.file import FileView
    return FileView

MatchViewSet = get_match_viewset()
PlayerViewSet = get_player_viewset()
PlayerTypeViewSet = get_player_type_viewset()
ScoreViewSet = get_score_viewset()
TeamViewSet = get_team_viewset()
UserViewSet = get_user_viewset()
FileView = get_file_view()