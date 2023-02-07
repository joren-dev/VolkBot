# Initialises all default events
from src.events.detail.default_events import *


# Manages the events
class EventManager:
    # Declare static member lists of event objects
    on_ready_events = []
    on_message_events = []

    def __init__(self):
        # Create & register events
        self.register_events()

    def register_events(self):
        # Please include the py module that contains your feature and create an instance
        # fmt: off
        from src.events.welcome_message import WelcomeMessage
        self.on_ready_events.append(WelcomeMessage())

        from src.events.print_message import PrintMessage
        self.on_message_events.append(PrintMessage())

        from src.events.language_filter import LanguageFilter
        self.on_message_events.append(LanguageFilter())
        # fmt: on
