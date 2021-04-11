import time
import json
import requests
from requests.packages.urllib3.util.url import parse_url
from bs4 import BeautifulSoup as bs4
from django.conf import settings


F_STORAGE = settings.BASE_DIR / 'url_query_files'


def get_all_links(url):
    url = parse_url(url)
    grab = requests.get(url)
    soup = bs4(grab.text, 'html.parser')
    f_name = url.host + ".json"
    f_path = F_STORAGE / f_name
    f = open(f_path, "w")
    counter = 0
    for link in soup.find_all("a"):
        data = link.get('href')
        if parse_url(data).host == url.host:
            try:
                session = requests.Session()
                session.cert = F_STORAGE / 'cacert.pem'
                req = requests.get(data, timeout=1)
                counter += 1

                to_dict = {
                    parse_url(data).path: {
                        'count': counter,
                        'STATUS CODE': str(req.status_code),
                        'SCHEME': parse_url(data).scheme,
                        'AUTH': parse_url(data).auth,
                        'PORT': parse_url(data).port
                    }
                }

                print(to_dict)
                f.write(json.dumps(to_dict, indent=4))
                f.write("\n")
            except Exception as e:
                counter += 1
                to_dict = {
                    parse_url(data).path: {
                        'count': counter,
                        'ERROR': type(e).__name__,
                        'SCHEME': parse_url(data).scheme,
                        'AUTH': parse_url(data).auth,
                        'PORT': parse_url(data).port
                    }
                }
                print(to_dict)
                f.write(json.dumps(to_dict, indent=4))
                f.write("\n")
    f.close()
    return f.name
