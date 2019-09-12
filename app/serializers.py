"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_match_serializer():
    from serializers.match import MatchSerializer
    return MatchSerializer

def get_player_serializer():
    from serializers.player import PlayerSerializer
    return PlayerSerializer

def get_player_type_serializer():
    from serializers.player_type import PlayerTypeSerializer
    return PlayerTypeSerializer

def get_score_serializer():
    from serializers.score import ScoreSerializer
    return ScoreSerializer

def get_team_serializer():
    from serializers.team import TeamSerializer
    return TeamSerializer

def get_user_serializer():
    from serializers.user import UserSerializer
    return UserSerializer

def get_file_serializer():
    from seed.serializers.helpers.file import FileSerializer
    return FileSerializer

MatchSerializer = get_match_serializer()
PlayerSerializer = get_player_serializer()
PlayerTypeSerializer = get_player_type_serializer()
ScoreSerializer = get_score_serializer()
TeamSerializer = get_team_serializer()
UserSerializer = get_user_serializer()
FileSerializer = get_file_serializer()
