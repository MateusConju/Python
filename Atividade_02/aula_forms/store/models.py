from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=100)
    market_share = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    platform = models.ManyToManyField(Platform)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Review(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE, 
        related_name="reviews"
    )

    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review para {self.game.name} - Nota {self.rating}"
