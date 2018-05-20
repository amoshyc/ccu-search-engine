import json
import time
import datetime

import bs4
import requests

HACKER_NEWS = 'https://news.ycombinator.com/front?day={}&p=1'


date = datetime.datetime.today()
urls = []
for _ in range(365):
    date = date - datetime.timedelta(days=1)
    hn_url = HACKER_NEWS.format(date.strftime('%Y-%m-%d'))
    print(hn_url)
    html = requests.get(hn_url).content
    dom = bs4.BeautifulSoup(html, 'lxml')
    elems = list(dom.find_all('a', class_='storylink'))
    print(len(elems))
    urls.extend([elem.get('href') for elem in elems])
    print('-' * 30)
    time.sleep(20)


with open('urls.json', 'w') as f:
    json.dump(urls, f, ensure_ascii=False, indent=1)
