"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_match_viewset():
    from seed.routes.matches import _MatchViewSet
    return _MatchViewSet

def get_player_viewset():
    from seed.routes.players import _PlayerViewSet
    return _PlayerViewSet

def get_player_position_viewset():
    from seed.routes.player_positions import _PlayerPositionViewSet
    return _PlayerPositionViewSet

def get_score_viewset():
    from seed.routes.scores import _ScoreViewSet
    return _ScoreViewSet

def get_team_viewset():
    from seed.routes.teams import _TeamViewSet
    return _TeamViewSet

def get_user_viewset():
    from seed.routes.users import _UserViewSet
    return _UserViewSet

def get_file_view():
    from seed.routes.files import FileView
    return FileView

MatchViewSet = get_match_viewset()
PlayerViewSet = get_player_viewset()
PlayerPositionViewSet = get_player_position_viewset()
ScoreViewSet = get_score_viewset()
TeamViewSet = get_team_viewset()
UserViewSet = get_user_viewset()
FileView = get_file_view()