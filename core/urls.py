from django.urls import path
from .views import index, get_urls, entry_list


app_name = 'core'
urlpatterns = [
    path('', index, name='index'),
    path('get-urls/', get_urls, name='get-urls'),
    path('entry-list/', entry_list, name="entry-list")
]
