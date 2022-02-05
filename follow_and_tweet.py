# importing libraries and modules
import tweepy
import time
import datetime
from config import create_api
from time import ctime


def public_tweets(api):
   
    try:

        #Wednesday tweet
        if datetime.date.today().weekday() == 3 and ctime()[11:16] == '14:30':

            daily_tweet = 'Hi there!\nCheck my TL for frequent and up-to-date #gischat tweets. Kindly offer help ' \
                           'where necessary! \nThank you! '

            api.update_status(daily_tweet)

            print('Wednesday tweet was successful')



    except tweepy.TweepyException:

        pass

def follow_followers(api):

    '''
        A follower function that
        checks to see if a follower is being followed,
        if not, gischatbot follows back

    '''

    for follower in tweepy.Cursor(api.get_followers).items():

        try:

            if not follower.following:

                USERNAME = follower.screen_name

                print(f'Following ->  {USERNAME}')

                follower.follow()

                print('Followed successfully')

            else:

                print('Followed all followers')

                break

        except  tweepy.TweepyException:

            print('Error occured while following user')
            time.sleep(900)


def main():
    api = create_api()
    while True:
        follow_followers(api)
        public_tweets(api)
        time.sleep(60)


if __name__ == '__main__':
    main()
