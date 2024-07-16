from logging import Logger

from slack_bolt import Ack
from slack_sdk import WebClient

def scheduled_message_callback(view, ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()
        provided_values = view["state"]["values"]
        logger.info(f"Provided values {provided_values}")
        time_to_summarize = provided_values["datetime_block_id"]["date_id"]["selected_date_time"] # Unix time
        channel = provided_values["select_channel_block_id"]["conversations_dropdown_id"]["selected_conversation"] # Channel id

        # PARSE DATE TIME TO FIGURE OUT WHAT TIME TO CALL COMMAND FUNCTION WITH
        time = 'Day'

        # Time over which summary will be issued
        summary_time = f"End of {time}"

        client.chat_scheduleMessage(channel=channel, post_at=time_to_summarize, text=f"{summary_time} Summary Incoming!")

    except Exception as e:
        logger.error(e)
