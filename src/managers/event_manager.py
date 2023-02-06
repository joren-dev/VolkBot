from discord.ext import commands

from src.utils.singleton import Singleton


# Warning: Unless you have a very good reason to use this class, please do not touch it.
class EventManager(commands.Bot, metaclass=Singleton):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        # Ensures commands work properly, wont process any commands without it.
        await self.process_commands(message)

        print(f"Message from {message.author}: {message.content}")
