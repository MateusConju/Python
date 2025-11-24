from django.contrib import admin
from .models import Products

# Register your models here.
class MonoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    search_fiels = ('nome',)

admin.site.register(Products)