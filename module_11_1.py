"""
module_11_1
"""

import requests as rq

URL1 = 'https://urban-university.ru/'
URL2 = 'https://teaofli.com/'
URL3 = 'https://requests.readthedocs.io/en/latest/'  # requests library docs
URLS = [URL1, URL2, URL3]
for number, url in enumerate(URLS):
    response = rq.get(url=url)
    headers = response.headers
    content = response.content
    text = response.text
    json = response.json
    encoding = response.encoding
    rc = response.status_code
    print(f"{number + 1}\nURL: {url}\nКод возврата: {rc}\nJSON: {json}\n")

