from django.shortcuts import render
import requests
from .models import ResponseCode


VICTIMS = [
    'https://djangoproject.com/',
    'https://pythonworld.ru/',
    'https://python.org/'
]


def index(request):
    for url in VICTIMS:
        resp = requests.get(url)
        ResponseCode.objects.create(url=url, code=resp.status_code)
    codes = ResponseCode.objects.all()
    template_name = 'core/index.html'
    context = {'codes': codes}
    return render(request, template_name, context)
