"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_player_viewset():
    try:
        from views.players import PlayerViewSet
        return PlayerViewSet
    except:
        from seed.views.players import _PlayerViewSet
        return _PlayerViewSet

def get_team_viewset():
    try:
        from views.teams import TeamViewSet
        return TeamViewSet
    except:
        from seed.views.teams import _TeamViewSet
        return _TeamViewSet

def get_user_viewset():
    try:
        from views.users import UserViewSet
        return UserViewSet
    except:
        from seed.views.users import _UserViewSet
        return _UserViewSet

def get_match_viewset():
    try:
        from views.matches import MatchViewSet
        return MatchViewSet
    except:
        from seed.views.matches import _MatchViewSet
        return _MatchViewSet

def get_score_viewset():
    try:
        from views.scores import ScoreViewSet
        return ScoreViewSet
    except:
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