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
                              "With *Summarizer*, you can get a summary of *any* channel's messages, *whenever* you want!\n" 
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
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "➕ Type `/invite @Summarizer`" 
                            + " in a *channel* or *group message* that you want to use it in:\n"
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
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": "Example: /invite @Summarizer"
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
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "➕ Use the `/summarize` command and specify *how long* you want a summary for:\n" 
                            + "        *>* Options:\n"
                            + "               *>* week\n"
                            + "               *>* _ days\n"
                            + "               *>* day\n"
                            + "               *>* _ hours\n"
                            + "               *>* hour\n"
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
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": "Example: /summarize 12 hours\n"
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
                        "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "Summarize command!",
                            "emoji": True
                        },
                        "image_url": "https://drive.google.com/uc?export=download&id=1WWJ8cmd3AMb_I-StseudMuEKQb6qB1Yv",
                        "alt_text": "Summarize command!"
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
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "➕ Hit the *Run shortcut* button or type / in a channel and click *Schedule summary* in the dropdown menu:\n" 
                            + "        *>* A modal will pop up!\n"
                            + "        *>* Go through the steps to select the \n"
                            + "               *>* *channel* you want a summary of,\n"
                            + "               *>* *time frame* of the summary (entire day's messages or entire week's messages), \n"
                            + "               *>* *frequency* of the summary (daily or weekly),\n"
                            + "               *>* *first and last date + time* you want the summaries published!\n"
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
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": "Example: /Schedule summary\n"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*That's it!*\nWait until the time(s) you designated and you will see your scheduled summaries!\n"
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
                        "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "Schedule summary!",
                            "emoji": True
                        },
                        "image_url": "https://drive.google.com/uc?export=download&id=17Vi3H4wGd4HRNpPjeItfwRZcD4ZBbujY",
                        "alt_text": "Schedule summary!"
                    },
                ],
            },
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
