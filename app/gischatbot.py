import tweepy
import time
from app.config import create_api
import logging

logger = logging.getLogger()

class Stream_Listener(tweepy.StreamListener):
    """Defines the tweet status and error state

    """

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        """Checks the status of the tweet. Mark it as favourite if not already done it and retweet if not already
        retweeted.

        :param tweet: tweet from listening to the stream
        """

        #  try to reply to mention or catch error
        logger.info(f"Processing tweet id {tweet.id}")
        # This tweet is a reply or I'm its author so, ignore it
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return 'Done'
        # Retweet, if not retweeted and set is_retweeted to True
        if hasattr(tweet, "retweeted_status"):
            is_retweeted = True
        else:

            try:
                tweet.retweet()
                time.sleep(2)
                tweet.favorite()
                print('Tweet retweeted and liked tweet:', tweet.text)

            except tweepy.TweepError as error:

                print(error, tweet.text)

    def on_error(self, status_code):

        """When encountering an error while listening to the stream, return False if `status_code` is 420 and print
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


def main(keyword):
    """Main method to initialize the api, create a Stream_Listener object to track tweets based on certain keywords and
    follow tweet owners.
    """
    api = create_api()
    print('Waiting for tweets...')
    my_stream_listener = Stream_Listener(api)
    my_stream = tweepy.Stream(auth=api.auth, listener=my_stream_listener)

    # , is_async=True, languages=["en"]
    my_stream.filter(track=keywords,languages=["en"])


if __name__ == '__main__':
    keywords = ["#GISCHAT", "#gischat", "#GISChat"]
    main(keywords)
