# importing the modules
from os import getenv
import tweepy
import logging


logger = logging.getLogger()
# authentication using Twitter API
# creating a function so that it can be used in other modules
def create_api():
    """
    This function collects the consumer and access keys, creates an api object and returns the authenticated api
    object.
    :return: authenticated api object
    """
    consumer_key = getenv('CONSUMER_KEY')
    consumer_secret = getenv('CONSUMER_SECRET')
    access_token = getenv('ACCESS_TOKEN')
    access_token_secret = getenv('ACCESS_TOKEN_SECRET')
    authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
    authentication.set_access_token(access_token, access_token_secret)
    api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return authenticate_api(api)

def authenticate_api(api):
    """This function verifies the credentials and returns the authenticated api object
    :param api: api object
    :return: authenticated api object
    :raises TweepError: raised due to an error Twitter Responded with or raised when an API method fails due to hitting
    Twitter’s rate limit.
    """
    try:
        api.verify_credentials()
    except tweepy.TweepError as error:
        logger.error("Error creating API", exc_info=True)
        raise error
    print("API is successfully created!")
    logger.info("API created")
    return api

#Getting Geo ID for Nigeria
#api=create_api()
#places = api.geo_search(query="Nigeria", granularity="country")
#print(places[0].id)

create_api()