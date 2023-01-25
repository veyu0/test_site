from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from main.models import Women

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Вход']


def index(request):
    posts = Women.objects.all()
    return render(request, 'main/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О сайте'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('Page not found')