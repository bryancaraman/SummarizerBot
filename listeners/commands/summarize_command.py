from slack_bolt import Ack, Respond
from logging import Logger
from .validate_input import validate_input
from .calculate_interval import calculate_interval

def summarize_command_callback(command, ack: Ack, respond: Respond, logger: Logger):
    try:
        ack()

        # Check for valid input
        input_response = validate_input(command['text'])
        if not input_response == 'Valid':
            respond(input_response)
            return
        
        respond(f"Summary of the last {command['text']}: ")

        # {command['channel_id']} for id of channel

        # Get messages within time interval
        oldest_time = calculate_interval(command['text'])
        
    except Exception as e:
        logger.error(e)
