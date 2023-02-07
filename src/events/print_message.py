from src.events.detail.event_base import OnMessageEvent


class PrintMessage(OnMessageEvent):
    async def on_message(self, message) -> None:
        print(f"Message {message.author}: {message.content}")
