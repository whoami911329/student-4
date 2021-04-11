from django.shortcuts import render


def receiver_room(request, room_name):
    return render(request,
                  'receiver/room.html',
                  {'room_name': room_name})
