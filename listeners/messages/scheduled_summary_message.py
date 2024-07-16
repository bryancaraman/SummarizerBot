

from logging import Logger
from slack_bolt import BoltContext, Say, Ack, Respond
from slack_sdk import WebClient

from ..commands import summarize_command_callback


def scheduled_summary_callback(context: BoltContext, client: WebClient, say: Say, logger: Logger):
    # Parse the context of the message
    channel = context['channel_id']
    message = context['matches'][0].split()
    time = message[2]

    # Produce summary based on message context
    summarize_command_callback({'text': time.lower(), 'channel_id': channel, 'schedule': 'True'}, Ack, Respond, logger)
