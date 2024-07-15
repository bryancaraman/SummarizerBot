from slack_sdk.errors import SlackApiError
from .message import Message
from .summarize_command import Logger

def process_message(message, client, channel_id, messages):
    text = message['text']
    ts = message['ts']

    try:
        link_response = client.chat_getPermalink(channel=channel_id, message_ts=ts)
        link = link_response['permalink']
        new_message = Message(text, link)
        messages.append(new_message)
    except SlackApiError as e:
        Logger.error("Error getting message link: {}".format(e))