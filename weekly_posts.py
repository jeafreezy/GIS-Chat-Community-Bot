import mastodon
import tweepy
from config import create_api, logging, WEEKLY_POST, tweet_time
import time


def weekly_posts(twitter_client, mastodon_client):
    """
    Sends weekly tweet on Twitter and Mastodon
    """
    try:
        if tweet_time():
            twitter_client.create_tweet(text=WEEKLY_POST)
            mastodon_client.status_post(status=WEEKLY_POST)
            logging.info("Weekly posts was sent successfully")
        logging.info("Not tweet day yet...")
    except (tweepy.TweepyException, mastodon.MastodonError) as error:
        logging.info(f"An error occurred while sending weekly tweet ->  {error}")


if __name__ == "__main__":
    twitter = create_api("twitter")
    mastodon = create_api("mastodon")
    while True:
        weekly_posts(twitter, mastodon)
        time.sleep(60 * 60 * 24)
