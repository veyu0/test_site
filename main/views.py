from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Main page')


def categories(request):
    return HttpResponse('<h1>Categories page</h1>')