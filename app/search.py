# This module searches through twitter for tweets with the hashtag #gis chat
from app.config import create_api
import tweepy
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

search_strings = ['#gischat', '#GISChat', '#GISCHAT']
api = create_api()


# function to handle twitter limits

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except  tweepy.RateLimitError:
        time.sleep(1000)


# A follow_followers function that accepts api and check if they are not followed, then follow them
def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()
        else:
            break

#A function that searches for a keyword and like and retweets it
def keyword_finder(api):

    for tweet in limit_handler(tweepy.Cursor(api.search, [search_string for search_string in search_strings]).items()):

        try:
            tweet.retweet()
            tweet.favorite()
            print('I liked and retweeted that tweet: \n', tweet.text)

        except (UnicodeEncodeError, tweepy.TweepError) as uni:
            print(uni)
            print(uni.reason)
        except StopIteration:
            break



def main():
    api = create_api()
    while True:
        keyword_finder(api)
        follow_followers(api)
        time.sleep(60)


if __name__ == "__main__":
    main()
