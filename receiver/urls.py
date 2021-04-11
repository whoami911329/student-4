from django.urls import path
from .views import receiver_room

app_name = 'receiver'
urlpatterns = [
    path('<room_name>/', receiver_room, name="receiver")
]
