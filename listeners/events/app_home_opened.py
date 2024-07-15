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
                            "text": "*Get Started:*\n"
                        },
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": 
                              "*1.* Invite Summarizer to a channel or group message that you want to use it in:\n" 
                            + "         *-* Example: */invite @Summarizer*\n"
                            + "*2.* Use the summarize command and specify how long you want a summary for:\n"
                            + "         *-* Options: \n"
                            + "                  *1.* week\n"
                            + "                  *2.* _ days\n"
                            + "                  *3.* day\n"
                            + "                  *4.* _ hours\n"
                            + "                  *5.* hour\n"
                            + "         *-* Example: */summarize day*\n"
                            + "*3.* Wait a few seconds until the summary displays in the channel!\n"
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
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "\n"
                        },
                    },
                ],
            },
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
