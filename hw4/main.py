from chromote import Chromote

from crawler import Crawler


chrome = Chromote()
crawler = Crawler('./html/', chrome)
crawler.fit([
    'https://edition.cnn.com/2018/05/20/europe/royal-wedding-harry-meghan-markle-day-after-intl/index.html/'
])
