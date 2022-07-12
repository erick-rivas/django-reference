"""
__Seed builder__
  AUTO_GENERATED Proxy (Read only)
  Modify via builder
"""

def get_match_viewset():
    import seed.routes.matches as SeedViewSet
    return SeedViewSet.MatchViewSet

def get_player_viewset():
    import seed.routes.players as SeedViewSet
    return SeedViewSet.PlayerViewSet

def get_player_position_viewset():
    import seed.routes.player_positions as SeedViewSet
    return SeedViewSet.PlayerPositionViewSet

def get_score_viewset():
    import seed.routes.scores as SeedViewSet
    return SeedViewSet.ScoreViewSet

def get_team_viewset():
    import seed.routes.teams as SeedViewSet
    return SeedViewSet.TeamViewSet

def get_user_viewset():
    import seed.routes.users as SeedViewSet
    return SeedViewSet.UserViewSet

def get_file_view():
    import seed.routes.files as SeedView
    return SeedView.FileView

MatchViewSet = get_match_viewset()
PlayerViewSet = get_player_viewset()
PlayerPositionViewSet = get_player_position_viewset()
ScoreViewSet = get_score_viewset()
TeamViewSet = get_team_viewset()
UserViewSet = get_user_viewset()
FileView = get_file_view()