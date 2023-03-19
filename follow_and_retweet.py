import logging
import tweepy
import time
from config import DELAY, create_api
from utils import WEEKLY_TWEET, tweet_time


class TwitterBot:
    """GIS CHAT TWITTER BOT"""

    def __init__(self, api_service) -> None:
        self.api_service = api_service

    def follow_followers(self):
        """
        Checks if a follower is being followed, otherwise, gischatbot follows back
        """
        for follower in tweepy.Cursor(self.api_service.get_followers).items():
            try:
                if not follower.following:
                    username = follower.screen_name
                    logging.info(f"Following ->  {username}")
                    follower.follow()
                    logging.info(f"Followed ->  {username}")
                else:
                    logging.info(f"Followed all followers")
                    break
            except tweepy.TweepyException as error:
                logging.info(f"An error occurred while following user ->  {error}")
                # sleep for a while
                time.sleep(DELAY)

    def weekly_tweet(self):
        """
        Sends weekly tweet on Twitter
        """
        try:
            if tweet_time():
                self.api_service.update_status(WEEKLY_TWEET)
                logging.info("Weekly tweet was sent successfully")
        except tweepy.TweepyException as error:
            logging.info(f"An error occurred while sending weekly tweet ->  {error}")

    def run_all(self):
        """
        Runs all the methods
        """
        while True:
            self.follow_followers()
            self.weekly_tweet()


if __name__ == "__main__":
    twitter_service = create_api("twitter")
    TwitterBot(api_service=twitter_service).run_all()
