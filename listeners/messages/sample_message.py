from logging import Logger

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient


def sample_message_callback(context: BoltContext, client: WebClient, say: Say, logger: Logger):
    pass
