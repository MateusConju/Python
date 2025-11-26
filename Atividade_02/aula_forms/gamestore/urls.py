from django.urls import path
from .views import (
    GameCreateView,
    GameListView,
    game_success,
    ReviewCreateView,
    ReviewListView,
    review_success
)

urlpatterns = [
    path('create/', GameCreateView.as_view(), name='game-create'),
    path('list/', GameListView.as_view(), name='game-list'),
    path('success/', game_success, name='game-success'),

    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/list/', ReviewListView.as_view(), name='review-list'),
    path('reviews/success/', review_success, name='review-success'),
]
