import os
import discord
import asyncio

from dotenv import load_dotenv

from src.managers.cog_system import CogSystem
from src.managers.discord_client import DiscordClient


# New python API update requires these
intents = discord.Intents.default()
intents.message_content = True

client = DiscordClient(command_prefix="!", intents=intents, help_command=None)


async def main():
    cog_system = CogSystem(client)
    await cog_system.reg_cogs()

    load_dotenv()
    # TODO: Check if file is present first
    token = os.getenv("TOKEN")
    if token is None:
        print("No token was provided in .env, shutting down...")
        exit(1)

    await client.start(token)


asyncio.run(main())
