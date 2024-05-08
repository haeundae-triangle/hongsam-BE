from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Game, Playlist
from .serializers import GameSerializer, PlaylistSerializer

# Create your views here.
@api_view(['GET'])
def game_detail(request, game_pk):
    game = Game.objects.get(pk=game_pk)
    serializer = GameSerializer(game)
    return Response(serializer.data)

@api_view(['GET'])
def game_top10(request):
    games = Game.objects.order_by('pk')[:10]
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def service_playlist(request):
    playlist = Playlist.objects.filter(from_service=1)
    serializer = PlaylistSerializer(playlist, many=True)
    return Response(serializer.data)