import tornado.ioloop
import tornado.web
from tornado.options import define, options
from tornado.httpserver import HTTPServer
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import facebook
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
		ACCESS_TOKEN = "Not"
		ACCESS_SECRET = "Something"
		CONSUMER_KEY = 	"Im"
		CONSUMER_SECRET = "Sharing"

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
		ACCESS_TOKEN = "Not"
		ACCESS_SECRET = "Something"
		CONSUMER_KEY = 	"Im"
		CONSUMER_SECRET = "Sharing"

		oauth = OAuth(ACCESS_TOKEN,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

		twitter = Twitter(auth = oauth)
		iterator = twitter.search.tweets(q="#Broncos", result_type="recent", lang="en", count = 10)

		self.render('twitterstream.html', twitterJSON = json.dumps(iterator))

class TwitterPOSTHandler(tornado.web.RequestHandler):
	def post(self):
		data = json.loads(self.request.body.decode('utf-8'))
		ACCESS_TOKEN = "Not"
		ACCESS_SECRET = "Something"
		CONSUMER_KEY = 	"Im"
		CONSUMER_SECRET = "Sharing"
		oauth = OAuth(ACCESS_TOKEN,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
		twitter = Twitter(auth = oauth)
		twitter.statuses.update(status = data)

class FacebookPostHandler(tornado.web.RequestHandler):
	def post(self):
		data = json.loads(self.request.body.decode('utf-8'))
		print(data)
		oauth = "Not for you, GitHub user"
		graph = facebook.GraphAPI(access_token = oauth, version ='2.2')
		graph.put_object(parent_object = 'me', connection_name='feed', message = data)


if __name__ == "__main__":
	settings={
		'static_path': 'static/',
		'site_port': 8080
	}
	routes = [
		(r"/", MainHandler),
		(r"/twitterstream", TwitterStreamHandler),
		(r"/twitterREST", TwitterRESTHandler),
		(r"/twitterPOST", TwitterPOSTHandler),
		(r"/facebookPOST", FacebookPostHandler)
	]
	application = tornado.web.Application(handlers=routes, **settings)
	server = HTTPServer(application, xheaders=True)
	server.bind(8080)
	server.start(0)
	tornado.ioloop.IOLoop.current().start()