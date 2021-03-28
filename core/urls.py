from django.urls import path
from .views import index, get_urls


urlpatterns = [
    path('', index, name='index'),
    path('get-urls/', get_urls, name='get-urls')
]
