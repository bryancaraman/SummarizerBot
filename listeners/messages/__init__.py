import re

from slack_bolt import App
from .scheduled_summary_message import scheduled_summary_callback


def register(app: App):
    app.message(re.compile("(End of Day Summary Incoming!|End of Week Summary Incoming!)"))(scheduled_summary_callback)
