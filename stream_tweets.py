import tweepy
import logging
import time
from config import (
    DELAY,
    FILTER_RULES,
    create_api,
)


class TweetStreamer(tweepy.StreamingClient):
    """TWEETS STREAMER"""

    def __init__(self) -> None:
        self.twitter_client: tweepy.Client = create_api("twitter")
        super(TweetStreamer, self).__init__(
            bearer_token=self.twitter_client.bearer_token
        )

    def on_connect(self):
        logging.info(f"Successfully connected to streaming API")

    def on_tweet(self, tweet):
        """
        Checks the status of the tweet. Like(i.e favourite) and retweet it if not already done
        """
        try:
            tweet_id = tweet.id

            self.twitter_client.retweet(tweet_id=tweet_id)
            logging.info(f"Tweet retweeted: {tweet} -- {tweet_id}")
            time.sleep(DELAY)
            self.twitter_client.like(tweet_id=tweet_id)
            logging.info(f"Tweet liked: {tweet} -- {tweet_id}")
        except tweepy.TweepyException as error:
            logging.info(f"An error occurred while retweeting -> {error}")

    def on_connection_error(self):
        logging.error(f"An error occurred while connecting to streaming service")

    def on_request_error(self, status_code):
        """
        When a status code that is non-200 is encountered
        """
        logging.error(f"An error occurred. Status code -> {status_code}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    stream = TweetStreamer()
    for hashtag in FILTER_RULES:
        stream.add_rules(tweepy.StreamRule(hashtag))
        logging.info(f"Added rule -> {hashtag}")
        time.sleep(DELAY)
    stream.filter()
