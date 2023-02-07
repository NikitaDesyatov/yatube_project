from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'Запись {slug}')
# Create your views here.
