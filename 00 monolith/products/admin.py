from django.contrib import admin
from.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    # 'prepopulated_fields' é a "magia" do admin que
    # preenche o slug automaticamente a partir do nome
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_available','updated_at')
    list_filter = ('is_available', 'category')
    list_editable = ('price', 'stock', 'is_available') # Permite edição rápida na lista
    search_fields = ('name', 'description')
