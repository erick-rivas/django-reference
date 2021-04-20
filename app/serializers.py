"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_match_serializer():
    import seed.serializers.match as SeedSerializer
    return SeedSerializer.MatchSerializer

def get_player_serializer():
    import seed.serializers.player as SeedSerializer
    return SeedSerializer.PlayerSerializer

def get_player_position_serializer():
    import seed.serializers.player_position as SeedSerializer
    return SeedSerializer.PlayerPositionSerializer

def get_score_serializer():
    import seed.serializers.score as SeedSerializer
    return SeedSerializer.ScoreSerializer

def get_team_serializer():
    import seed.serializers.team as SeedSerializer
    return SeedSerializer.TeamSerializer

def get_user_serializer():
    import seed.serializers.user as SeedSerializer
    return SeedSerializer.UserSerializer

def get_file_serializer():
    import seed.serializers.file as SeedSerializer
    return SeedSerializer.FileSerializer

MatchSerializer = get_match_serializer()
PlayerSerializer = get_player_serializer()
PlayerPositionSerializer = get_player_position_serializer()
ScoreSerializer = get_score_serializer()
TeamSerializer = get_team_serializer()
UserSerializer = get_user_serializer()
FileSerializer = get_file_serializer()