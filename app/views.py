"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_player_viewset():
    from views.players import PlayerViewSet
    return PlayerViewSet

def get_team_viewset():
    from views.teams import TeamViewSet
    return TeamViewSet

def get_user_viewset():
    from seed.views.users import _UserViewSet
    return _UserViewSet

def get_match_viewset():
    from seed.views.matches import _MatchViewSet
    return _MatchViewSet

def get_score_viewset():
    from seed.views.scores import _ScoreViewSet
    return _ScoreViewSet

def get_file_view():
    from seed.views.helpers.file import FileView
    return FileView

PlayerViewSet = get_player_viewset()
TeamViewSet = get_team_viewset()
UserViewSet = get_user_viewset()
MatchViewSet = get_match_viewset()
ScoreViewSet = get_score_viewset()
FileView = get_file_view()