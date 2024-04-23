from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Game
from .serializers import GameSerializer

# Create your views here.
@api_view(['GET'])
def game_detail(request, game_pk):
    game = Game.objects.get(pk=game_pk)
    serializer = GameSerializer(game)
    return Response(serializer.data)