"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_player_serializer():
    from serializers.player import PlayerSerializer
    return PlayerSerializer

def get_team_serializer():
    from serializers.team import TeamSerializer
    return TeamSerializer

def get_user_serializer():
    from seed.serializers.user import _UserSerializer
    return _UserSerializer

def get_match_serializer():
    from seed.serializers.stats.match import _MatchSerializer
    return _MatchSerializer

def get_score_serializer():
    from seed.serializers.stats.score import _ScoreSerializer
    return _ScoreSerializer

def get_file_serializer():
    from seed.serializers.helpers.file import FileSerializer
    return FileSerializer

PlayerSerializer = get_player_serializer()
TeamSerializer = get_team_serializer()
UserSerializer = get_user_serializer()
MatchSerializer = get_match_serializer()
ScoreSerializer = get_score_serializer()
FileSerializer = get_file_serializer()