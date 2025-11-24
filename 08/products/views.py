from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Products

# Create your views here.
def hello_world(request):
    contexto = {'username': 'Aluno Senior'}
    return render(request, 'hello.html', contexto)

def product_list_simple(request):
    produtos = Products.objects.all()
    contexto = {'produtos': produtos}
    return render(request, 'product_list.html', contexto)

def ProductListView(ListView): 
    model = Products