from slack_bolt import App
from .scheduled_message import scheduled_message_callback


def register(app: App):
    app.view("scheduled_message_id")(scheduled_message_callback)
