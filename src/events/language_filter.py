from src.events.detail.event_base import OnMessageEvent
from src.globals.client_instance import DiscordClient


class LanguageFilter(OnMessageEvent):
    # TODO: Ship them in a file, and create the ability to add/remove words runtime.
    kBadWordsList = ["kanker", "flikker", "can3cer"]

    async def on_message(self, message) -> None:
        for bad_word in self.kBadWordsList:
            if bad_word in message.content.lower():
                await message.delete()
                await message.channel.send(
                    f"Hey {message.author.mention}, keep it civil blud."
                )
                break
