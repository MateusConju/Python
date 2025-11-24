from django.urls import path
from .views import hello_world, product_list_simple, ProductListView

urlpatterns = [
    path('hello/', hello_world),
    path('simpleproducts/', product_list_simple),
    path('listview/', ProductListView.as_view()),
]

