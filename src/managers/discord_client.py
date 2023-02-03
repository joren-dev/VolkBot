from discord.ext import commands


class DiscordClient(commands.Bot):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        # Ensures commands work properly, wont process any commands without it.
        await self.process_commands(message)

        print(f"Message from {message.author}: {message.content}")
