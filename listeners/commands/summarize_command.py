import os
from slack_bolt import Ack, Respond
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from logging import Logger
from .validate_input import validate_input
from .calculate_interval import calculate_interval
from .get_summary import get_summary
from .message import Message

client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))

def summarize_command_callback(command, ack: Ack, respond: Respond, logger: Logger):
    try:
        ack()

        # Check for valid input
        input_response = validate_input(command['text'])
        if not input_response == 'Valid':
            respond(input_response)
            return
        
        respond(f"Summary of the last {command['text']}: ")

        # Calculate when the time interval for getting messages
        oldest_time = calculate_interval(command['text'])
        
        channel_id = command['channel_id']
        conversation_history = []

        try:
            result = client.conversations_history(channel=channel_id, inclusive=True, oldest=oldest_time)
            conversation_history = result['messages']
        except SlackApiError as e:
            logger.error("Error getting conversation: {}".format(e))

        # STRETCH GOAL: GET MESSAGES IN THREADS AS WELL

        # Get array in order from oldest message to newest message
        conversation_history.reverse()

        messages = []

        print(conversation_history)

        # IF USERNAME IS WANTED FOR MORE SPECIFIC SUMMARY, WARNING: TAKES LONG
        # user_data = client.users_profile_get(user=message['user'])
        # user = user_data['profile']['real_name']

        for message in conversation_history:
            if message['type'] == 'message':
                text = message['text']
                ts = message['ts']
                new_message = Message(text, ts)
                messages.append(new_message)

        if len(messages) == 0:
            respond(f"No messages within the last {command['text']}")

        summary = get_summary(messages)

        respond(summary)
        
    except Exception as e:
        logger.error(e)
