import datetime
import time


def tweet_time() -> bool:
    return datetime.date.today().weekday() == 3 and time.ctime()[11:16] == "14:30"


WEEKLY_TWEET: str = (
    "Hi there!\nCheck my TL for frequent and up-to-date #gischat tweets. Kindly offer help "
    "where necessary! \nThank you! "
)
