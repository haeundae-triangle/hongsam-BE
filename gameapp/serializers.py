from rest_framework import serializers
from .models import Game, Playlist

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__' 


class PlaylistDetailSerializer(serializers.ModelSerializer):
    games = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = '__all__'

    def get_games(self, obj):
        games = Game.objects.filter(gameplaylist__playlist=obj)
        serializer = GameSerializer(games, many=True)
        return serializer.data