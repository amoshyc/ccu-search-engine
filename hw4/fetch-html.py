import json
import time
import urllib
import pathlib
from itertools import chain

import bs4
from selenium import webdriver

out_dir = pathlib.Path('./raw/')
out_dir.mkdir(exist_ok=True)
driver = webdriver.Chrome('./chromedriver')

with open('./urls.json') as f:
    data = json.load(f)
urls = list(chain.from_iterable(stories for date, stories in data.items()))

for uid, url in enumerate(urls):
    print(f'{uid:05d}:{url}', end='...')
    if (out_dir / f'{uid:05d}.html').exists():
        print('pass')
        continue

    # parse
    meta = urllib.parse.urlparse(url)
    if meta.netloc == '':
        continue

    # Fetch html
    time0 = time.time()
    driver.get(url)
    html = driver.page_source
    time1 = time.time()
    dom = bs4.BeautifulSoup(html, 'lxml')
    time2 = time.time()

    # Save
    with (out_dir / f'{uid:05d}.html').open('w') as f:
        f.write(dom.prettify())
        f.write('\n')
    with (out_dir / f'{uid:05d}.json').open('w') as f:
        json.dump({
            'url': url,
            'fetch_time': time1 - time0,
            'parse_time': time2 - time1,
        }, f, ensure_ascii=False, indent=1)

    print('OK')
