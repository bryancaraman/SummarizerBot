import os
from slack_bolt import Ack, Respond
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from logging import Logger
from .validate_input import validate_input
from .calculate_interval import calculate_interval
from .get_summary import get_summary
from .message import Message
from .process_message import process_message

client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))

def summarize_command_callback(command, ack: Ack, respond: Respond, logger: Logger):
    try:
        ack()

        # Check for valid input
        input_response = validate_input(command['text'])
        if not input_response == 'Valid':
            respond(input_response)
            return
        
        respond(f"Summary of the last {command['text']}... ")

        # Calculate when the time interval for getting messages
        oldest_time = calculate_interval(command['text'])
        
        channel_id = command['channel_id']
        conversation_history = []

        try:
            result = client.conversations_history(channel=channel_id, inclusive=True, oldest=oldest_time)
            conversation_history = result['messages']
        except SlackApiError as e:
            logger.error("Error getting conversation: {}".format(e))

        # Get array in order from oldest message to newest message
        conversation_history.reverse()

        messages = []

        # IF USERNAME IS WANTED FOR MORE SPECIFIC SUMMARY
        # WARNING: API CALL NEEDED FOR EACH MESSAGE, i.e. ALREADY LONG BUT EVEN LONGERRRRR
        # Future: Implement in specificity mode?
        # user_data = client.users_profile_get(user=message['user'])
        # user = user_data['profile']['real_name']

        for message in conversation_history:
            if message['type'] == 'message':
                # If there is a thread
                if 'thread_ts' in message:
                    # Get thread replies
                    replies = client.conversations_replies(channel=channel_id, ts=message['thread_ts'])
                    for reply in replies['messages']:
                        process_message(reply, client, channel_id, messages)
                    continue

                process_message(message, client, channel_id, messages)

        if len(messages) == 0:
            respond(f"No messages within the last {command['text']}.")
            return

        # Get summary from AI
        summary = get_summary(messages)

        # Display summary for user
        respond(summary)
        
    except Exception as e:
        logger.error(e)
