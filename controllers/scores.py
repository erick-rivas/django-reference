from rest_framework import generics

from models.score import Score
from models.serializers.score import ScoreSerializer

class SaveScore(generics.CreateAPIView):
    serializer_class = ScoreSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)