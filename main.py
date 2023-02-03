import os
import discord
import asyncio
from discord.ext import commands


class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")
    
    async def on_message(self, message):
        # Ensures commands work properly, wont process any commands without it.
        await self.process_commands(message)

        print(f"Message from {message.author}: {message.content}")

# New python API update requires these
intents = discord.Intents.default()
intents.message_content = True

client = Client(command_prefix="!", intents=intents, help_command=None)

async def load_cogs():
    # TODO: Ensure this is only loaded in debug mode, not in live
    # Remote code execution module for debugging purposes
    await client.load_extension("jishaku")

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load_cogs()
    await client.start("my token goes here")

asyncio.run(main())
