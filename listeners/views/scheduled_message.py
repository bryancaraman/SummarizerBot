from logging import Logger

from slack_bolt import Ack
from slack_sdk import WebClient

import datetime
import math

def scheduled_message_callback(view, ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()
        provided_values = view["state"]["values"]
        logger.info(f"Provided values {provided_values}")
        channel = provided_values["select_channel_id"]["conversations_dropdown_id"]["selected_conversation"]
        time = provided_values["gkpwh"]["summary_time_action"]["selected_option"]["text"]["text"]
        frequency = provided_values["OdRfW"]["summary_frequency_action"]["selected_option"]["text"]["text"]
        first_date = provided_values["first_summary_id"]["first_date_id"]["selected_date_time"]
        last_date = provided_values["qF4hb"]["last_date_id"]["selected_date"]

        summary_time = f"End of {time}"

        last_date = last_date.split('-')
        year = int(last_date[0])
        month = int(last_date[1])
        day = int(last_date[2])
        last_date = int(datetime.datetime(year, month, day, 0, 0).strftime('%s'))
        last_date += 86400

        if (last_date - first_date < 0):
            client.chat_postMessage(channel=channel, text=f"Can't choose a final date earlier than the first date.")
            return

        cur_date = first_date

        if (frequency == "Daily"):
            days_to_summarize = math.ceil((last_date - first_date) / 86400)
            for i in range(0, days_to_summarize):
                try:
                    client.chat_scheduleMessage(channel=channel, post_at=cur_date, text=f"{summary_time} Summary Incoming!")
                except:
                    client.chat_postMessage(channel=channel, text=f"Can't choose a starting time in the past or at the current minute.")
                    return
                cur_date += 86400
        else:
            weeks_to_summarize = math.ceil((last_date - first_date) / 604800)
            for i in range(0, weeks_to_summarize):
                try:
                    client.chat_scheduleMessage(channel=channel, post_at=cur_date, text=f"{summary_time} Summary Incoming!")
                except:
                    client.chat_postMessage(channel=channel, text=f"Can't choose a starting time in the past or at the current minute.")
                    return
                cur_date += 604800

        client.chat_postMessage(channel=channel, text=f"{frequency} summaries scheduled!")

    except Exception as e:
        logger.error(e)
