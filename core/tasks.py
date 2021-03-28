import requests
from time import sleep
from celery import shared_task
from datetime import datetime
from .models import Entry


VICTIMS = [
    'https://djangoproject.com/',
    'https://pythonworld.ru/',
    'https://python.org/'
]


@shared_task
def crawl_response():
    for url in VICTIMS:
        result = requests.get(url)
        timestamp = datetime.now().strftime(
            format=("%d/%m/%Y at %H:%M:%S"))
        print({'url': url,
               'response': result,
               'timestamp': timestamp})
        Entry.objects.create(
            url=url,
            status_code=result.status_code,
            date_time=timestamp,
        )
        sleep(2)


def get_method_name(**kwargs):
    default = {'method': 'unrecognized',
               'sender_func': 'unspecified',
               'depth': 0}

    for key in list(kwargs.keys()):
        if key in default.keys():
            if kwargs[key] == '':
                kwargs[key] = default.get(key)
        else:
            kwargs.pop(key)
    default.update(kwargs)
    return f'calling "{default.get("method")}" from {default.get("sender_func")}'


@shared_task
def update_response():
    pass


if not Entry.objects.all():
    print('no objects in database! if i find some, i write it in database...')
    crawl_response()


while True:
    sleep(3)
    update = update_response
    update()
    print(get_method_name(method=update.__name__, sender_func="while"))
