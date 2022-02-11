
import tweepy
import time
from os import getenv
from config import create_api
CONSUMER_KEY = getenv('CONSUMER_KEY')
CONSUMER_SECRET = getenv('CONSUMER_SECRET')
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = getenv('ACCESS_TOKEN_SECRET')



class StreamListener(tweepy.Stream):

    """       
        Listens to current tweets with the keywords to retweet and like
    """
  
    def on_status(self, tweet):

        """
            Checks the status of the tweet. Like(favourite)it if not already done it and retweet if not already
            retweeted.

            :param tweet: tweet from listening to the stream
        """
        api=create_api()

        try:

            api.retweet(tweet.id)

            time.sleep(5)

            api.create_favorite(tweet.id)

            print('Tweet retweeted and liked', )

        except tweepy.TweepyException as error:

           pass

    def on_request_error(self, status_code):

        """
            When encountering an error  with a status code greater than 400, sleep for a while
        """
        if status_code >= 400:
            time.sleep(900)


def main(keywords):
    """
        Main method to initialize the api, create a StreamListener object to track tweets based on certain keywords and
        follow tweet owners.
    """

    print('Waiting for tweets...')

    stream_listener = StreamListener(
        CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET
    )

    stream_listener.filter(track=keywords, languages=["en"] )


if __name__=='__main__':

    keywords = ["#GISCHAT", "#gischat", "#GISChat", '#gisChat', '#mappymeme','#GISCHATS','@gischatbot','#spatialnode','#Spatialnode']

    main(keywords)



