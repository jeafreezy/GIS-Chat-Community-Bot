# importing the modules
from os import getenv
import tweepy

CONSUMER_KEY = getenv('CONSUMER_KEY')
CONSUMER_SECRET = getenv('CONSUMER_SECRET')
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = getenv('ACCESS_TOKEN_SECRET')


def create_api():

    """
        This function collects the consumer and access keys, creates an api object and returns the authenticated api
        object.
        :return: authenticated api object
    """


    authentication = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    api = tweepy.API(authentication, wait_on_rate_limit=True,retry_count=3, retry_delay=2)

    return api


