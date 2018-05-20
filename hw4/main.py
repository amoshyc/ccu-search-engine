from chromote import Chromote

from crawler import Crawler


chrome = Chromote()
crawler = Crawler('./html/', chrome)
crawler.fit([
    'https://news.ycombinator.com/'
])
