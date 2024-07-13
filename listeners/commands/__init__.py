from slack_bolt import App
from .summarize_command import summarize_command_callback


def register(app: App):
    app.command("/summarize")(summarize_command_callback)
