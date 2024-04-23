from django.urls import path
from . import views

app_name = 'gameapp'

urlpatterns = [
 path('<int:game_pk>/', views.game_detail)
]
