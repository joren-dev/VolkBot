from src.events.detail.event_base import OnReadyEvent
from src.globals.client_instance import DiscordClient


class WelcomeMessage(OnReadyEvent):
    async def on_ready(self) -> None:
        print(f"Logged on as {DiscordClient().user}!")
