from django.urls import path
from . import views

app_name = 'gameapp'

urlpatterns = [
 path('<int:game_pk>/', views.game_detail),
 path('top10/', views.game_top10),
 path('servicePlaylist/', views.service_playlist),
 path('servicePlaylist/<int:playlist_pk>/', views.service_playlist_detail),
]
