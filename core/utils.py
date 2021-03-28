import requests
from bs4 import BeautifulSoup
from django.conf import settings


def get_all_links(url):
    grab = requests.get(url)
    soup = BeautifulSoup(grab.text, 'html.parser')
    f_name = url.lstrip(
        f"{'https', 'http'}://www.").rstrip(f"{'.org/', '.com/'}") + ".txt"
    f_path = settings.BASE_DIR / 'url_files' / f_name
    f = open(f_path, "w")
    for link in soup.find_all("a"):
        data = link.get('href')
        if data is None:
            continue
        f.write(data)
        f.write("\n")
    f.close()
    return f.name
