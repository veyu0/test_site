from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse('Main page')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Categories page</h1><p>{cat_id}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Page not found')