import os
import wikipedia
import tornado.ioloop
import tornado.web

CACHING_DIR = "cached"

from techniques.numbers import adjust_numbers
from techniques.markov import markov_replace
from techniques.pos import pos_filter

lying_ways = [
    markov_replace
]

def get_article_cached(article):
    cached_files = os.listdir(CACHING_DIR)
    article_path = os.path.join(CACHING_DIR, article)
    if article in cached_files:
        with open(article_path, "r") as article_file:
            return article_file.read()
    else:
        try:
            article_data = wikipedia.page(article).summary.encode("ascii", "ignore")
        except:
            raise Exception("Couldn't retrieve content for article.")
        with open(article_path, "w") as article_file:
            article_file.write(article_data)
        return article_data


default_deception = 3
def falsify(article, deception_levels):
    output = article
    for technique in lying_ways:
        if len(deception_levels) > 0:
            deception_level = deception_levels.pop()
        else:
            deception_level = default_deception
        output = technique(output, deception_level)
    if not output.endswith("."):
        output += "."
    return output


class LyingHandler(tornado.web.RequestHandler):
    def get(self, article):
        deception_levels = [default_deception for x in range(len(lying_ways))]
        try:
             deception_levels = [int(i) for i in self.get_query_arguments("data", strip=True)[0].split(",")]
        except:
            pass
        print "Fetching article for %s with evils %s" % (article, deception_levels)
        self.write(falsify(get_article_cached(article), deception_levels))


application = tornado.web.Application([
    (r"/wiki/(.*)", LyingHandler),
])

if __name__ == "__main__":

    print "Starting lying as a service."

    if not os.path.exists(CACHING_DIR):
        os.makedirs(CACHING_DIR)

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()