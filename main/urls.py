from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, about, pageNotFound

urlpatterns = [
    path('', index),
    path('about/', about),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound