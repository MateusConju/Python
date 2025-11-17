from django.shortcuts import render, HttpResponse

# Create your views here.
def product_list_view(request):
    return HttpResponse('<h1>Testando</h1>')
