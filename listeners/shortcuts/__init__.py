from slack_bolt import App
from .schedule_summary import schedule_summary_callback


def register(app: App):
    app.shortcut("schedule_summary_id")(schedule_summary_callback)
