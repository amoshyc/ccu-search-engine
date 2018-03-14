import time
import json
import pathlib

import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class SearchHandler(tornado.web.RequestHandler):
    def post(self):
        query = self.get_argument('query')
        print(query)
        self.write({})


class MoreHandler(tornado.web.RequestHandler):
    def post(self):
        item1 = {
            'url':
            'http://travel.ettoday.net/article/1.htm',
            'title':
            '外星人回到地球了　ETtoday.net Come homeddddddddddddddddddddddddddddddddddddddddddddddddd',
            'body':
            '記者吳光中／台北報導 熄燈3年半，ETtoday回來了，這次不叫「達康」，改叫「達內」，如果把ETtoday.net的net解釋為new ET，倒也還蠻有趣的；既然叫new ET，總要有點創新吧？是的，ETtoday.net要運用「酷新聞」的實驗成果，走向群眾、擁抱社群，懷著真誠的心與網友互動，「樂在分享　愛上雲端」。 現實場景：2011年10月3日ETtoday.net的記者們陸續報到，這是個細雨飛的早晨，9點正，總裁王令麟及董事長馬詠睿站在公司門口迎接這群新員工，他一一握手完畢後笑說：'
        }
        item2 = {'url': 'https://example.org', 'title': 't2', 'body': 'abc'}
        self.write({
            'len': 6,
            'res': [
                item1,
                item1,
                item1,
                item1,
                item1,
                item1,
            ]
        })


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