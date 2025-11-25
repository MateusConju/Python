from django.db import models

# Create your models here.
class Category(models.Model):
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=110, unique=True, help_text="Nome amigavel para URLs, ex 'eletrõnicos")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome