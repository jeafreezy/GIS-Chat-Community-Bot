import tweepy
from config import create_api, logging, WEEKLY_TWEET, tweet_time
import time


class TwitterBot:
    """GIS CHAT TWITTER BOT"""

    def __init__(self) -> None:
        self.twitter_client = create_api("twitter")

    def weekly_tweet(self):
        """
        Sends weekly tweet on Twitter
        """
        try:
            if tweet_time():
                self.twitter_client.create_tweet(text=WEEKLY_TWEET)
                logging.info("Weekly tweet was sent successfully")
            logging.info("Not tweet day yet...")
        except tweepy.TweepyException as error:
            logging.info(f"An error occurred while sending weekly tweet ->  {error}")


if __name__ == "__main__":
    while True:
        TwitterBot().weekly_tweet()
        time.sleep(60 * 60 * 24)
