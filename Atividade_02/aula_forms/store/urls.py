from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameListView.as_view(), name='game-list'),
    path('new/', views.GameCreateView.as_view(), name='game-create'),
    path('new/success', views.game_success, name='game-success'),
]