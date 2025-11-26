from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Game, Review
from .forms import ReviewForm

class GameCreateView(CreateView):
    model = Game
    fields = ['name', 'platform', 'price', 'score']
    success_url = 'success'


class GameListView(ListView):
    model = Game
    context_object_name = 'games'

    def get_queryset(self):
        queryset = Game.objects.all().prefetch_related('platform')
        return queryset


def game_success(request):
    return render(request, 'store/game_success.html')

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'store/review_form.html'
    success_url = 'review-success'


class ReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'store/review_list.html'

    def get_queryset(self):
        return Review.objects.select_related('game').all()


def review_success(request):
    return render(request, 'store/review_success.html')
