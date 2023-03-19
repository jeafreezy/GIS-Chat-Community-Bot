import tweepy
import logging
import time
from config import (
    DELAY,
    create_api,
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET,
)
from utils import KEYWORDS


class TweetStreamer(tweepy.Stream):
    """TWEETS STREAMER"""

    def __init__(self) -> None:
        self.api_service = create_api("twitter")
        super(TweetStreamer, self).__init__(
            consumer_key=TWITTER_CONSUMER_KEY,
            consumer_secret=TWITTER_CONSUMER_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_TOKEN_SECRET,
        )

    def on_status(self, tweet):
        """
        Checks the status of the tweet. Like(i.e favourite) and retweet it if not already done
        """
        try:
            self.retweet(id=tweet.id)
            logging.info(f"Tweet retweeted: {id}")
            time.sleep(DELAY)
            self.api_service.create_favorite(id=tweet.id)
            logging.info(f"Tweet liked: {id}")
        except tweepy.TweepyException as error:
            logging.info(f"An error occurred while retweeting -> {error}")

    def on_request_error(self, status_code):
        """
        When encountering an error  with a status code greater than 400, sleep for a while
        """

        if status_code >= 400:
            logging.info(f"An error occurred. Status code -> {status_code}")
            # sleep for a while
            time.sleep(DELAY)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    TweetStreamer().filter(track=KEYWORDS, languages=["en"])
