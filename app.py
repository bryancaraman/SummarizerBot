import os
import logging

from config import SLACK_APP_TOKEN
from config import SLACK_BOT_TOKEN

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from listeners import register_listeners

# Initialization
app = App(token=SLACK_BOT_TOKEN, ignoring_self_events_enabled=False)
logging.basicConfig(level=logging.DEBUG)

# Register Listeners
register_listeners(app)

# Start Bolt app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
