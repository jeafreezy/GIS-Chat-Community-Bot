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
                logging.info(f"Status liked successfully->{status_id}")
                time.sleep(DELAY)
                self.mastodon_client.status_reblog(status_id)
                logging.info(f"Status boosted successfully->{status_id}")
        except MastodonError as error:
            logging.error(f"An error occured while interacting with post -> {error}")


if __name__ == "__main__":
    mastodon_instance = create_api("mastodon")
    mastodon_instance.stream_public(
        listener=MastodonStreamListener(mastodon_instance), remote=True
    )
    mastodon_instance.stream_public(
        listener=MastodonStreamListener(mastodon_instance), local=True
    )
