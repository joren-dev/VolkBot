from src.events.detail.event_base import OnMessageEvent
from src.globals.client_instance import DiscordClient


class LanguageFilter(OnMessageEvent):
    async def on_message(self, message) -> None:
        if message.content == "kanker":
            await message.channel.send("Doe is rustig broertje.")
