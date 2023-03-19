from os import getenv
import tweepy
from typing import Union
from mastodon import Mastodon


TWITTER_CONSUMER_KEY = getenv("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = getenv("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = getenv("TWITTER_ACCESS_TOKEN_SECRET")
MASTODON_ACCESS_TOKEN = getenv("MASTODON_ACCESS_TOKEN")
MASTODON_CLIENT_ID = getenv("MASTODON_CLIENT_ID")
MASTODON_CLIENT_SECRET = getenv("MASTODON_CLIENT_SECRET")
MASTODON_BASE_URL = getenv("MASTODON_BASE_URL")
DELAY = int(getenv("DELAY", "1000"))


def create_api(social_network: str) -> Union[tweepy.API, Mastodon]:
    """
    This function creates an authenticated instance for the provided social network

    """

    if social_network == "twitter":
        authentication = tweepy.OAuth1UserHandler(
            TWITTER_CONSUMER_KEY,
            TWITTER_CONSUMER_SECRET,
            TWITTER_ACCESS_TOKEN,
            TWITTER_ACCESS_TOKEN_SECRET,
        )
        twitter_service = tweepy.API(
            authentication, wait_on_rate_limit=True, retry_count=3, retry_delay=2
        )
        return twitter_service
    if social_network == "mastodon":
        mastodon_service = Mastodon(
            client_id=MASTODON_CLIENT_ID,
            client_secret=MASTODON_CLIENT_SECRET,
            access_token=MASTODON_ACCESS_TOKEN,
            api_base_url=MASTODON_BASE_URL,
        )
        return mastodon_service
