import logging
from os import getenv
import tweepy
from typing import Union
from mastodon import Mastodon
import datetime
import time

TWITTER_CONSUMER_KEY = getenv("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = getenv("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = getenv("TWITTER_ACCESS_TOKEN_SECRET")
MASTODON_ACCESS_TOKEN = getenv("MASTODON_ACCESS_TOKEN")
MASTODON_CLIENT_ID = getenv("MASTODON_CLIENT_ID")
MASTODON_CLIENT_SECRET = getenv("MASTODON_CLIENT_SECRET")
MASTODON_BASE_URL = getenv("MASTODON_BASE_URL")
DELAY = int(getenv("DELAY", "3"))
TWITTER_BEARER_TOKEN = getenv("TWITTER_BEARER_TOKEN")
FILTER_RULES = [
    "#GISCHAT",
    "#gischat",
    "#GISChat",
    "#gisChat",
    "#mappymeme",
    "#GISCHATS",
    "#spatialnode",
    "#Spatialnode",
    "@gischatbot",
    "#geospatial",
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


logging.basicConfig(level=logging.INFO)


def tweet_time() -> bool:
    return datetime.date.today().weekday() == 3 and time.ctime()[11:16] == "14:30"


WEEKLY_TWEET: str = (
    "Hi there!\nCheck my TL for frequent and up-to-date #gischat tweets. Kindly offer help "
    "where necessary! \nThank you! "
)
