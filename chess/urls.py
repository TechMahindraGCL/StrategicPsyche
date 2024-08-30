from django.urls import path
from . import views

urlpatterns = [
    path('', views.chess_dashboard, name='chess_dashboard'),  # Chess dashboard view
    path('game/', views.play_chess, name='play_chess'),  # Chess game page
]
