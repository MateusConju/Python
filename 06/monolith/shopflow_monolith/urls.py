from django.urls import path
from . import views

urlPatterns = [
    path('', view.product_list_value, name='product')
]