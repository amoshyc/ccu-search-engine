import json
import time
import pathlib
import collections
import urllib

import bs4

class Crawler(object):
    def __init__(self, out_dir, chrome):
        self.out_dir = pathlib.Path(out_dir)
        self.out_dir.mkdir(exist_ok=True)
        self.chrome = chrome

    def _request(self, url):
        for tab in self.chrome.tabs:
            self.chrome.close_tab(tab)

        tab = self.chrome.add_tab(url)
        self.chrome.close_tab(tab)
        html = tab.html
        self.chrome.close_tab(tab)

        return html

    def _parse(self, url, html):
        dom = bs4.BeautifulSoup(html, 'lxml')
        url_meta = urllib.parse.urlparse(url)

        def expand(link):
            link_meta = urllib.parse.urlparse(link)
            if link_meta.scheme not in ['http', 'https', '']:
                return '', False
            if link_meta.netloc == '':
                link_meta = link_meta._replace(netloc=url_meta.netloc)
            if link_meta.scheme == '':
                link_meta = link_meta._replace(scheme=url_meta.scheme)
            link = link_meta.geturl()
            link = link + '/' if link[-1] != '/' else link
            return link, True

        links = [link.get('href') for link in dom.find_all('a')]
        links = [link for link, ok in map(expand, links) if ok]
        return dom.html, links

    def _save(self, uid, dom, meta):
        html_path = self.out_dir / f'{uid:08d}.html'
        json_path = self.out_dir / f'{uid:08d}.meta.json'

        with html_path.open('w') as f:
            f.write(dom.prettify())
            f.write('\n')
        with json_path.open('w') as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)


    def fit(self, urls):
        queue = set(urls)
        deque = collections.deque(urls)

        uid = 0
        while len(deque) > 0 and uid < 1:
            url = deque.popleft()

            print('{}'.format(url), end=' ... ')
            start_time = time.time()

            html = self._request(url)
            dom, links = self._parse(url, html)

            end_time = time.time()
            elapsed = end_time - start_time
            print('{:.2f}s'.format(elapsed))

            self._save(uid, dom, {
                'uid': uid,
                'url': url,
                'links': links,
                'elapsed': elapsed
            })
            uid += 1

            for link in links:
                if link not in queue:
                    queue.add(link)
                    deque.append(link)

