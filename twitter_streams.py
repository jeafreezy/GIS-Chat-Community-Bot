import re
import tweepy
import time
from config import DELAY, FILTER_RULES, create_api, logging


class TweetStreamer(tweepy.StreamingClient):
    """This class inherits from tweepy Streaming Client to access live tweets from Twitter with the specified filter rules i.e hashtags"""

    def __init__(self) -> None:
        self.twitter_client: tweepy.Client = create_api("twitter")
        super(TweetStreamer, self).__init__(
            bearer_token=self.twitter_client.bearer_token
        )

    def on_connect(self):
        logging.info(f"Successfully connected to streaming API")

    def on_tweet(self, tweet):
        """
        Checks the status of the tweet. Like and retweet it
        """
        try:
            # to prevent the bot from retweeting replies under a tweet without the hastags
            tags_regex = re.compile("|".join(FILTER_RULES))
            if tags_regex.search(tweet.text):
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
    stream = TweetStreamer()
    previous_rules = stream.get_rules().data
    if previous_rules:
        logging.info(f"Rules already exist -> {previous_rules}")
    else:
        for hashtag in FILTER_RULES:
            stream.add_rules(tweepy.StreamRule(hashtag))
            logging.info(f"Added rule -> {hashtag}")
            time.sleep(DELAY)
    try:
        stream.filter()
    except KeyboardInterrupt:
        stream.session.close()
        stream.on_disconnect()
        stream.running = False
        logging.warning("Keyboard Interrupt. Closing connection...")
