from django.test import TestCase
from django.urls import reverse
from .models import Game, Platform, Review


class GameModelTest(TestCase):
    def setUp(self):
        self.platform = Platform.objects.create(name="PC", market_share=50)

    def test_game_creation(self):
        game = Game.objects.create(
            name="Doom",
            score=90,
            price=59.99
        )
        game.platform.add(self.platform)

        self.assertEqual(Game.objects.count(), 1)
        self.assertEqual(game.name, "Doom")
        self.assertIn(self.platform, game.platform.all())


class ReviewModelTest(TestCase):
    def setUp(self):
        self.platform = Platform.objects.create(name="PC", market_share=50)
        self.game = Game.objects.create(name="Review Game", score=85, price=49.99)
        self.game.platform.add(self.platform)

    def test_review_creation(self):
        review = Review.objects.create(game=self.game, rating=8, comment="Ótimo jogo!")
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(review.game, self.game)
        self.assertEqual(review.rating, 8)

    def test_review_cascade_delete(self):
        Review.objects.create(game=self.game, rating=7, comment="Bahia")
        self.assertEqual(Review.objects.count(), 1)

        # Delecao do game deve remover as reviews
        self.game.delete()
        self.assertEqual(Review.objects.count(), 0)


class ReviewViewsTest(TestCase):
    def setUp(self):
        self.platform = Platform.objects.create(name="PS5", market_share=40)
        self.game = Game.objects.create(name="View Game", score=75, price=39.99)
        self.game.platform.add(self.platform)

    def test_review_create_view(self):
        url = reverse('review-create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<form")

    def test_review_list_view(self):
        Review.objects.create(game=self.game, rating=9, comment="Muito bom")

        url = reverse('review-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Muito bom")
        self.assertContains(response, "View Game")
