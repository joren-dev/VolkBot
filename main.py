import os
import discord
import asyncio
from discord.ext import commands


class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")


intents = discord.Intents.default()
intents.message_content = True

client = Client(command_prefix="!", intents=intents)

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load_cogs()
    await client.start("my token goes here")

asyncio.run(main())
