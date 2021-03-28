from django.shortcuts import render, redirect
from .models import Entry
from .utils import get_all_links


def index(request):
    template_name = 'core/index.html'
    return render(request, template_name, {'codes': Entry.objects.all()})


def get_urls(request):
    url = str(request.GET.get('url'))
    get_all_links(url)
    return redirect('get-urls')

# https://www.geeksforgeeks.org/
