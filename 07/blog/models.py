from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField()

class Tag(models.Model):
    nome = models.CharField(max_length=10)

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    publicado_em = models.DateTimeField(auto_now_add=True)
    eh_destaque = models.BooleanField(default=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='artigos', default=1)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.titulo

class ProdutoFinanceiro(models.Model):
    nome = models.CharField(max_length=100)
    ticker = models.CharField(max_length=5, unique=True, db_index=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

