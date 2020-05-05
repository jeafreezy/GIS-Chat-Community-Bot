import tweepy
import time
from app.config import create_api
import datetime
from time import ctime
import random


class Stream_Listener(tweepy.StreamListener):
    """
    Defines the tweet status and error state
    Listens to current tweets with the keywords to retweet and like

    """

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):

        """
        Checks the status of the tweet. Like(favourite)it if not already done it and retweet if not already
        retweeted.

        :param tweet: tweet from listening to the stream
        """

        # If the tweet is a reply or I'm its author , ignore it

        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:

            return 'Done'

        # Retweet, if not retweeted and set is_retweeted to True

        if hasattr(tweet, "retweeted_status"):

            is_retweeted = True

        else:

            try:
                tweet.retweet()
                time.sleep(5)
                tweet.favorite()
                print('Tweet retweeted and liked tweet:', tweet.text)

            except tweepy.TweepError as error:

                print(error, tweet.text)

    def on_error(self, status_code):

        """
        When encountering an error while listening to the stream, return False if `status_code` is 420 and print
        the error.

        :param status_code:
        :return: False when `status_code` is 420 to disconnect the stream.

        """
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False
        elif status_code == 429:
            time.sleep(900)
        else:
            print(tweepy.TweepError, status_code)


#Frequent tweets when it's 30 minutes to #gischat

def public_tweets(api):

    if datetime.date.today().weekday() == 2 and ctime()[11:16] == '19:30':

        time_difference_dict = 'GMT-> 19:00' + '\n' + 'CDT-> 14:00' + '\n' + 'WAT -> 20:00'

        tweet_to_publish = [
            f'Hello everyone,it\'s almost time for #gischat :) \n Check your timezone below: \n {time_difference_dict}',
            f'Hi everyone, it\'s #gischat in 30minutes :) \n Check your timezone below: \n {time_difference_dict}',
            f'Hi there,don\'t forget it\'s almost #gischat time! \n Check your timezone below: \n {time_difference_dict}']

        random_tweet = random.choice(tweet_to_publish)

        api.update_status(random_tweet)

    else:

        try:

            #Tweet every day

            limit = 60 * 60 * 24

            frequent_tweet ='Check my TL for frequent and up-to-date #gischat tweets. Kindly offer help where necessary! \nThank you!'

            api.update_status(frequent_tweet)

            print('Tweeted successfully')

            time.sleep(limit)

        except tweepy.TweepError as e:

            print('Error Message : ' , e)

# function to handle twitter limits
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except  tweepy.RateLimitError:
        time.sleep(1000)


# A follow_followers function that accepts api and check if they are not followed, then follow them
def follow_followers(api):
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        if not follower.following:
            print(f'Following ->  {follower.name}')
            follower.follow()
        else:
            break


def main(keywords):
    """Main method to initialize the api, create a Stream_Listener object to track tweets based on certain keywords and
    follow tweet owners.
    """
    api = create_api()
    print('Waiting for tweets...')
    my_stream_listener = Stream_Listener(api)
    my_stream = tweepy.Stream(auth=api.auth, listener=my_stream_listener)
    public_tweets(api)
    follow_followers(api)
    # , is_async=True, languages=["en"]
    my_stream.filter(track=keywords, languages=["en"])


if __name__ == '__main__':
    keywords = ["#GISCHAT", "#gischat", "#GISChat", '#gisChat', '#gisCHAT']
    main(keywords)
