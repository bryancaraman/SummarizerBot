from listeners import commands
from listeners import events
from listeners import messages
from listeners import shortcuts
from listeners import views


def register_listeners(app):
    commands.register(app)
    events.register(app)
    messages.register(app)
    shortcuts.register(app)
    views.register(app)
