from django.shortcuts import render
from django.http import JsonResponse

def product_list_view(request):
    data = {'msg': 'Hello World!'}
    return JsonResponse(data)

def product_path_param(id):
    data = {'msg': "Você retornou um produto de id:", "id":id}
    return JsonResponse(data)

def product_query_param(request):
    teste = request.GET.get('teste')
    au = request.GET
    data = {'teste': teste, 'ali':au}
    return JsonResponse(data)