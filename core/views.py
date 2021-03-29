from django.shortcuts import render
from .models import Entry
from .tasks import fetch_links
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# rest_framework imports
from rest_framework.generics import ListAPIView


def index(request):
    template_name = 'core/index.html'
    return render(request, template_name)


def entry_list(request):
    template_name = 'core/entry_list.html'
    return render(request, template_name,
                  {'entry_list': Entry.objects.all()})


def get_urls(request):
    url = str(request.GET.get('url'))
    fetch_links.delay(url)
    return HttpResponseRedirect(
        reverse_lazy('core:entry-list'))
