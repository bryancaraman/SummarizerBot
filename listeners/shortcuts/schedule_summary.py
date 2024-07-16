from logging import Logger

from slack_bolt import Ack
from slack_sdk import WebClient


def schedule_summary_callback(body: dict, ack: Ack, client: WebClient, logger: Logger):
    try:
        ack()
        client.views_open(
            trigger_id=body["trigger_id"],
            view={
                "type": "modal",
                "callback_id": "scheduled_message_id",
                "title": {"type": "plain_text", "text": "Schedule summary"},
                "blocks": [
                    {
                        "block_id": "select_channel_block_id",
                        "type": "input",
                        "label": {
                            "type": "plain_text",
                            "text": "Select the channel you want to summarize:",
                        },
                        "element": {
                            "type": "conversations_select",
                            "action_id": "conversations_dropdown_id",
                            "response_url_enabled": True,
                        },
                    },
                    {
                        "type": "input",
                        "block_id": "datetime_block_id",
                        "label": {
                            "type": "plain_text",
                            "text": "When do you want to see the summary?",
                        },
                        "element": {
                            "type": "datetimepicker",
                            "action_id": "date_id",
                        },
                    },
                ],
                "submit": {"type": "plain_text", "text": "Submit"},
            },
        )
    except Exception as e:
        logger.error(e)
