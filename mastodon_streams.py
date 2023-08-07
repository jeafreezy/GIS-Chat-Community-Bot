import time
from mastodon import Mastodon, StreamListener, MastodonError
from config import DELAY, FILTER_RULES, create_api, logging
import re


class MastodonStreamListener(StreamListener):
    """This class inherits from mastodon stream listener to access live posts to retweet and like"""

    def __init__(self, mastodon_instance: Mastodon) -> None:
        self.mastodon_client = mastodon_instance
        super().__init__()

    def on_update(self, status):
        # remove filters since mastodon does not support filtering streams with # or @
        valid_tags = [
            tag.split("#")[1] if "#" in tag else tag.split("@")[1]
            for tag in FILTER_RULES
        ]
        tags_regex = re.compile("|".join(valid_tags))
        try:
            if tags_regex.search(str(status.content).lower()):
                status_id = status.id
                self.mastodon_client.status_favourite(status_id)
                logging.info(f"Status liked successfully ->{status_id}")
                time.sleep(DELAY)
                self.mastodon_client.status_reblog(status_id)
                logging.info(f"Status boosted successfully->{status_id}")
        except MastodonError as error:
            logging.error(f"An error occured while interacting with post -> {error}")


def local_stream():
    """Connect to the local streams"""
    mastodon_instance = create_api("mastodon")
    mastodon_instance.stream_public(
        listener=MastodonStreamListener(mastodon_instance), local=True
    )


def remote_stream():
    """Connect to remote servers"""
    mastodon_instance = create_api("mastodon")
    mastodon_instance.stream_public(
        listener=MastodonStreamListener(mastodon_instance), remote=True
    )


if __name__ == "__main__":
    # local_process = multiprocessing.Process(
    #     target=local_stream,
    # )
    # local_process.start()
    # remote_process = multiprocessing.Process(
    #     target=remote_stream,
    # )
    # remote_process.start()
    # local_process.join()
    # remote_process.join()
    local_stream()
    # remote_stream()
