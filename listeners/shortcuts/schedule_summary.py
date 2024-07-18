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
                        "block_id": "select_channel_id",
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
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Day or Week",
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Day",
                                    },
                                    "value": "value-0"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Week",
                                    },
                                    "value": "value-1"
                                },
                            ],
                            "action_id": "summary_time_action"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Do you want summaries of the entire day's messages or the entire week's messages?",
                        }
                    },
                    {
                        "type": "input",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Daily or Weekly",
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Daily",
                                    },
                                    "value": "value-0"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Weekly",
                                    },
                                    "value": "value-1"
                                },
                            ],
                            "action_id": "summary_frequency_action"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "How often should summaries repeat?",
                        }
                    },
                    {
                        "type": "input",
                        "block_id": "first_summary_id",
                        "label": {
                            "type": "plain_text",
                            "text": "When do you want to see the first summary?",
                        },
                        "element": {
                            "type": "datetimepicker",
                            "action_id": "first_date_id",
                        },
                    },
                    {
                        "type": "input",
                        "element": {
                            "type": "datepicker",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select a date.",
                            },
                            "action_id": "last_date_id"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "When do you want the last summary?",
                        }
                    },
                ],
                "submit": {"type": "plain_text", "text": "Submit"},
            },
        )
    except Exception as e:
        logger.error(e)
