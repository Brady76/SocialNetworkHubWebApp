import tornado.ioloop
import tornado.web
from tornado.options import define, options
from tornado.httpserver import HTTPServer
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json
import simplejson as json

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("GET gud")
		self.render('index.html')
	def post(self):
		self.write("POSTing up")

class TwitterStreamHandler(tornado.web.RequestHandler):
	def get(self):
		ACCESS_TOKEN = "874249651-S1SofEKsa3CFzhrxy0tbEj3DxxXuNVBPYR03oxyj"
		ACCESS_SECRET = "S53SzgFJ6R9k9awgaMErTn90dyUUrOfzdm3fqUxFEnzVq"
		CONSUMER_KEY = 	"Zb18h6djL2I61LSrJGQDR4PbD"
		CONSUMER_SECRET = "5xNWaF4sOhY9rrBkOdBIiREDUJXoyC9rcQY49US0U61mlutVlS"

		oauth = OAuth(ACCESS_TOKEN,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

		twitter_stream = TwitterStream(auth = oauth)

		iterator = twitter_stream.statuses.filter(track = "Von Miller", language = "en")

		tweet_count = 5

		tweet_array = []
		for tweet in iterator:
			tweet_count -= 1
			tweet_array.append(tweet)
			if tweet_count <= 0:
				break

		self.render('twitterstream.html', twitterJSON = tweet_array)

class TwitterRESTHandler(tornado.web.RequestHandler):
	def get(self):
		ACCESS_TOKEN = "874249651-S1SofEKsa3CFzhrxy0tbEj3DxxXuNVBPYR03oxyj"
		ACCESS_SECRET = "S53SzgFJ6R9k9awgaMErTn90dyUUrOfzdm3fqUxFEnzVq"
		CONSUMER_KEY = 	"Zb18h6djL2I61LSrJGQDR4PbD"
		CONSUMER_SECRET = "5xNWaF4sOhY9rrBkOdBIiREDUJXoyC9rcQY49US0U61mlutVlS"

		oauth = OAuth(ACCESS_TOKEN,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

		twitter = Twitter(auth = oauth)
		iterator = twitter.search.tweets(q="#Broncos", result_type="recent", lang="en", count = 10)

		print(json.dumps(iterator, indent=4))
			

		self.render('twitterstream.html', twitterJSON = json.dumps(iterator))

class TwitterPOSTHandler(tornado.web.RequestHandler):
	def post(self):
		ACCESS_TOKEN = "874249651-S1SofEKsa3CFzhrxy0tbEj3DxxXuNVBPYR03oxyj"
		ACCESS_SECRET = "S53SzgFJ6R9k9awgaMErTn90dyUUrOfzdm3fqUxFEnzVq"
		CONSUMER_KEY = 	"Zb18h6djL2I61LSrJGQDR4PbD"
		CONSUMER_SECRET = "5xNWaF4sOhY9rrBkOdBIiREDUJXoyC9rcQY49US0U61mlutVlS"

		oauth = OAuth(ACCESS_TOKEN,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
		twitter = Twitter(auth = oauth)
		iterator = twitter.statuses.update(status = "Tweeting through Tornado, because this is what I do when I'm bored now, apparently.")


if __name__ == "__main__":
	settings={
		'static_path': 'static/',
		'site_port': 8080
	}
	routes = [
		(r"/", MainHandler),
		(r"/twitterstream", TwitterStreamHandler),
		(r"/twitterREST", TwitterRESTHandler),
		(r"/twitterPOST", TwitterPOSTHandler)
	]
	application = tornado.web.Application(handlers=routes, **settings)
	server = HTTPServer(application, xheaders=True)
	server.bind(8080)
	server.start(0)
	tornado.ioloop.IOLoop.current().start()