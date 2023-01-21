from django.urls import path
from .views import index, categories, pageNotFound

urlpatterns = [
    path('', index),
    path('categories/<int:cat_id>/', categories),
]

handler404 = pageNotFound