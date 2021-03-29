import time
import json
import certifi
import requests
from bs4 import BeautifulSoup
from django.conf import settings

from urllib3.exceptions import (MaxRetryError,
                                NewConnectionError,
                                ConnectionError)
from requests.exceptions import ReadTimeout, SSLError


# default var

# ERRORS = (MaxRetryError, NewConnectionError,
#           ConnectionError, SSLError, ReadTimeout)


def get_all_links(url):

    grab = requests.get(url)
    soup = BeautifulSoup(grab.text, 'html.parser')

    f_name = url.lstrip(
        f"{'https://', 'http://'}{'www.', ''}").rstrip(
            f"{'.org/', '.com/'}") + ".json"
    f_path = settings.BASE_DIR / 'url_files' / f_name
    f = open(f_path, "w")
    counter = 0
    for link in soup.find_all("a"):
        data = link.get('href')
        if data is not None:
            if data.startswith("http://") or data.startswith("https://"):
                try:
                    counter += 1
                    req_session = requests.Session()
                    req_session.cert = '/mnt/sda2/backup/dev/STUDENTS/mL-proj/env/lib/python3.8/site-packages/certifi/cacert.pem'
                    req = requests.get(
                        data,
                        # cert=certifi.where(),
                        allow_redirects=False,
                        timeout=4
                    )

                    writable = json.dumps({counter: {
                        'URL': data,
                        'CODE': req.status_code
                    }}, indent=2)

                    print(writable)

                    f.write(writable)
                    f.write("\n")

                except ReadTimeout:
                    print('Read ttttttimeout')

                except SSLError:
                    print('SSLError')

                except MaxRetryError:
                    print('max-retry EXEPTION')

                except NewConnectionError:
                    print('New Connect')

                except ConnectionError:
                    print('Connection eRRor')

                except TimeoutError:
                    print('timeOUTError')

                except BaseException:
                    time.sleep(3)
                    print("here is ass of a world")
    f.close()
    return f.name
