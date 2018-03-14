import time
import pathlib

import tornado.ioloop
import tornado.web

from elasticsearch import Elasticsearch

es = Elasticsearch()
query = {
    "size": 10,
    "query": {
        "query_string": {
            "query": '*',
        }
    },
    "highlight": {
        "fields": {
            "body": {}
        }
    },
    "sort": [
        { '_score': 'desc' },
        { '_id': 'asc' }
    ],
} # yapf: disable


def flatten(hit):
    return {
        'title': hit['_source']['title'],
        'url': hit['_source']['url'],
        'body': '……'.join(hit['highlight']['body']) + ' …',
    }


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class SearchHandler(tornado.web.RequestHandler):
    def post(self):
        global query, from_
        query['query']['query_string']['query'] = self.get_argument('query')
        res = es.search(index='ettoday', doc_type='news', body=query)
        from_ = 0
        self.write({
            'total': res['hits']['total'],
        })


class MoreHandler(tornado.web.RequestHandler):
    def post(self):
        global query, from_
        res = es.search(
            index='ettoday', doc_type='news', body=query, from_=from_)
        self.write({
            'len': len(res['hits']['hits']),
            'data': list(flatten(hit) for hit in res['hits']['hits'])
        })
        from_ += 10


def main():
    route = [
        (r'/', IndexHandler),
        (r'/more', MoreHandler),
        (r'/search', SearchHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler, { 'path': './static' }),
    ] # yapf: disable

    app = tornado.web.Application(route, debug=True)

    app.listen(8787)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()