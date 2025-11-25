from django.contrib import admin, views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products/", views.product_path_param()),
    path("query/", views.product_query_param())
]
