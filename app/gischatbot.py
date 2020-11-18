import tweepy
import time
from app.config import create_api

class Stream_Listener(tweepy.StreamListener):
    """
    Defines the tweet status and error state
    Listens to current tweets with the keywords to retweet and like

    """

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):

        """
        Checks the status of the tweet. Like(favourite)it if not already done it and retweet if not already
        retweeted.

        :param tweet: tweet from listening to the stream
        """

        try:
            tweet.retweet()
            time.sleep(5)
            tweet.favorite()
            print('Tweet retweeted and liked tweet:', tweet.text)

        except tweepy.TweepError as error:

            print(error, tweet.text)


    def on_error(self, status_code):

        """
        When encountering an error while listening to the stream, return False if `status_code` is 420 and print
        the error.

        :param status_code:
        :return: False when `status_code` is 420 to disconnect the stream.

        """
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False
        elif status_code == 429:
            time.sleep(900)
        else:
            print(tweepy.TweepError, status_code)


def main(keywords):
    """
    Main method to initialize the api, create a Stream_Listener object to track tweets based on certain keywords and
    follow tweet owners.
    """
    api = create_api()

    print('Waiting for tweets...')
    my_stream_listener = Stream_Listener(api)
    my_stream = tweepy.Stream(auth=api.auth, listener=my_stream_listener)
    my_stream.filter(track=keywords, languages=["en"] )



if __name__=='__main__':

    keywords = ["#GISCHAT", "#gischat", "#GISChat", '#gisChat', #GISDay,#gisday,#GISDAY, '#gisCHAT', '#gischats', 'GISChats', '#gisCHATs',
                '#GISCHATS','#geospatial','@gischatbot']

    main(keywords)



