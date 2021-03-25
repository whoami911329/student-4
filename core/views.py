from django.shortcuts import render
import requests
from .models import Entry


VICTIMS = [
    'https://djangoproject.com/',
    'https://pythonworld.ru/',
    'https://python.org/'
]


def index(request):
    for url in VICTIMS:
        resp = requests.get(url)
        Entry.objects.create(url=url, status_code=resp.status_code)
    codes = Entry.objects.all()
    template_name = 'core/index.html'
    context = {'codes': codes}
    return render(request, template_name, context)
