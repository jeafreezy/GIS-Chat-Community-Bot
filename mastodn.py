from mastodon import Mastodon,StreamListener

from config import MASTODON_ACCESS_TOKEN, MASTODON_BASE_URL, MASTODON_CLIENT_ID, MASTODON_CLIENT_SECRET






class MastodonStreamListener(StreamListener):
   """This class inherits from mastodon stream listener to access live streams to retweet and like"""
   ... 

#fetch tweet streams
#like tweets
#follow followers
#
if __name__=='__main__':
   # mastodon_instance.status_post("hello world!")
   ...