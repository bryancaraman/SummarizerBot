from logging import Logger


def app_home_opened_callback(client, event, logger: Logger):
    # ignore the app_home_opened event for anything but the Home tab
    if event["tab"] != "home":
        return
    try:
        client.views_publish(
            user_id=event["user"],
            view={
                "type": "home",
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Welcome to Summarizer!",
                        },
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": 
                              "With *Summarizer*, you can get a summary of *any* channel's messages, *whenever* you want!\n\n" 
                              + "Either use the *summarize command* yourself, or *schedule summaries* to appear at any time!"
                        },
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Get Started:\n"
                        },
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                    {
                        "type": "rich_text",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "emoji",
                                        "name": "arrow_right"
                                    },
                                    {
                                        "type": "text",
                                        "text": "  Invite Summarizer to a ",
                                    },
                                    {
                                        "type": "text",
                                        "text": "channel",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": " or ",
                                    },
                                    {
                                        "type": "text",
                                        "text": "group message",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": " that you want to use it in:\n",
                                    },
                                ]
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                    {
			            "type": "rich_text",
			            "elements": [
				            {
                                "type": "rich_text_quote",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "/invite @Summarizer\n"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Summarize Command:\n"
                        },
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                    {
                        "type": "rich_text",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "emoji",
                                        "name": "arrow_right"
                                    },
                                    {
                                        "type": "text",
                                        "text": "  Use the ",
                                    },
                                    {
                                        "type": "text",
                                        "text": "summarize",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": " command and specify ",
                                    },
                                    {
                                        "type": "text",
                                        "text": "how long",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": " you want a summary for:\n",
                                    },
                                    {
                                        "type": "text",
                                        "text": "        >",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": " Options: \n",
                                    },
                                    {
                                        "type": "text",
                                        "text": "                 >",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": "  week\n",
                                    },
                                    {
                                        "type": "text",
                                        "text": "                 >",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": "  _ days\n",
                                    },
                                    {
                                        "type": "text",
                                        "text": "                 >",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": "  day\n",
                                    },
                                    {
                                        "type": "text",
                                        "text": "                 >",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": "  _ hours\n",
                                    },
                                    {
                                        "type": "text",
                                        "text": "                 >",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": "  hour\n",
                                    },
                                ]
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                    {
			            "type": "rich_text",
			            "elements": [
				            {
                                "type": "rich_text_quote",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "/summarize 12 hours\n"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": 
                              "*That's it!*\nWait a few seconds until the summary displays in the channel!\n"
                        },
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Schedule Summaries:\n"
                        },
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                    {
                        "type": "rich_text",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "emoji",
                                        "name": "arrow_right"
                                    },
                                    {
                                        "type": "text",
                                        "text": "  Hit the ",
                                    },
                                    {
                                        "type": "text",
                                        "text": "Run Shortcut",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": " button or type / in a channel and click ",
                                    },
                                    {
                                        "type": "text",
                                        "text": "Schedule Summary",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": " in the dropdown menu.\n",
                                    },
                                    {
                                        "type": "text",
                                        "text": "       > A modal will pop up!\n",
                                    },
                                    {
                                        "type": "text",
                                        "text": "       > Go through the steps to select the \n            > ",
                                    },
                                    {
                                        "type": "text",
                                        "text": " channel ",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": " you want a summary of, the \n            > ",
                                    },
                                    {
                                        "type": "text",
                                        "text": "time frame",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": " of the summary (end of day or end of week), the \n            > ",
                                    },
                                    {
                                        "type": "text",
                                        "text": "frequency",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": " of the summary (daily or weekly), as well as the \n            > ",
                                    },
                                    {
                                        "type": "text",
                                        "text": "first/last date and time",
                                        "style": {
                                            "bold": True
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": " you want it published!\n",
                                    },
                                ]
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                    {
			            "type": "rich_text",
			            "elements": [
				            {
                                "type": "rich_text_quote",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "/Schedule summary\n"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": 
                              "*That's it!*\nWait until the time(s) you designated and you will see your scheduled summary!\n"
                        },
                    },
                ],
            },
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
