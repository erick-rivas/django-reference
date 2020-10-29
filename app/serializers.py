"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_match_serializer():
    from seed.serializers.match import _MatchSerializer
    return _MatchSerializer

def get_player_serializer():
    from seed.serializers.player import _PlayerSerializer
    return _PlayerSerializer

def get_player_position_serializer():
    from seed.serializers.player_position import _PlayerPositionSerializer
    return _PlayerPositionSerializer

def get_score_serializer():
    from seed.serializers.score import _ScoreSerializer
    return _ScoreSerializer

def get_team_serializer():
    from seed.serializers.team import _TeamSerializer
    return _TeamSerializer

def get_user_serializer():
    from seed.serializers.user import _UserSerializer
    return _UserSerializer

def get_file_serializer():
    from seed.serializers.helpers.file import FileSerializer
    return FileSerializer

MatchSerializer = get_match_serializer()
PlayerSerializer = get_player_serializer()
PlayerPositionSerializer = get_player_position_serializer()
ScoreSerializer = get_score_serializer()
TeamSerializer = get_team_serializer()
UserSerializer = get_user_serializer()
FileSerializer = get_file_serializer()