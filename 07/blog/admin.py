from django.contrib import admin
from .models import Autor, Artigo, Tag

# Register your models here.
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado_em', 'eh_destaque')
    search_fiels = ('titulo', 'conteudo')
    list_fielter = ('eh_destaque', 'autor_nome')

admin.site.register(Autor)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Tag)
