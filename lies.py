import os
import wikipedia
import tornado.ioloop
import tornado.web

CACHING_DIR = "cached"

from techniques.numbers import adjust_numbers
from techniques.pos import pos_filter

lying_ways = [
    adjust_numbers,
    pos_filter
]

def get_article_cached(article):
    cached_files = os.listdir(CACHING_DIR)
    article_path = os.path.join(CACHING_DIR, article)
    if article in cached_files:
        with open(article_path, "r") as article_file:
            return article_file.read()
    else:
        try:
            article_data = wikipedia.page(article).content
        except:
            raise Exception("Couldn't retrieve content for article.")
        with open(article_path, "w") as article_file:
            article_file.write(article_data.encode("UTF-8"))
        return article_data


def falsify(article):
    output = article
    for technique in lying_ways:
        output = technique(output)
    return output


class LyingHandler(tornado.web.RequestHandler):
    def get(self, article):
        print "Fetching article for %s" % article
        self.write(falsify(get_article_cached(article)))


application = tornado.web.Application([
    (r"/(.*)", LyingHandler),
])

if __name__ == "__main__":

    print "Starting lying as a service."

    if not os.path.exists(CACHING_DIR):
        os.makedirs(CACHING_DIR)

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
