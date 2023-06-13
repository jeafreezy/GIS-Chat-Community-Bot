import logging
import tweepy
from typing import Union
from mastodon import Mastodon
from decouple import config

TWITTER_CONSUMER_KEY = config("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = config("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = config("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = config("TWITTER_ACCESS_TOKEN_SECRET")
MASTODON_ACCESS_TOKEN = config("MASTODON_ACCESS_TOKEN")
MASTODON_CLIENT_ID = config("MASTODON_CLIENT_ID")
MASTODON_CLIENT_SECRET = config("MASTODON_CLIENT_SECRET")
MASTODON_BASE_URL = config("MASTODON_BASE_URL")
DELAY = int(config("DELAY", "3"))
TWITTER_BEARER_TOKEN = config("TWITTER_BEARER_TOKEN")

FILTER_RULES = [
    "#gischat",
    "#mappymeme",
    "#gischats",
    "@gischatbot",
    "#geospatial",
    "#gischatbot",
]


def create_api(social_network: str) -> Union[tweepy.Client, Mastodon]:
    """
    This function creates an authenticated instance for the provided social network

    """

    if social_network == "twitter":
        twitter_client = tweepy.Client(
            bearer_token=TWITTER_BEARER_TOKEN,
            wait_on_rate_limit=True,
            consumer_key=TWITTER_CONSUMER_KEY,
            consumer_secret=TWITTER_CONSUMER_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_TOKEN_SECRET,
        )

        return twitter_client
    if social_network == "mastodon":
        mastodon_service = Mastodon(
            client_id=MASTODON_CLIENT_ID,
            client_secret=MASTODON_CLIENT_SECRET,
            access_token=MASTODON_ACCESS_TOKEN,
            api_base_url=MASTODON_BASE_URL,
        )
        return mastodon_service


logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(asctime)s:%(message)s")
