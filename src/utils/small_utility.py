import os
import os.path
import discord

from dotenv import load_dotenv

from src.managers.discord_client import DiscordClient
from src.managers.cog_system import CogSystem


# TODO: Impl proper error handling
def get_env_token(req_token):
    # Check if .env file is present & at least one environment variable is set.
    if load_dotenv() is False:
        print(".env file is not present, shutting down...")
        exit(1)

    # Check if specified .env token is present in .env file
    token = os.getenv(req_token)
    if token is None:
        print("Couldnt find requested token in .env, shutting down...")
        exit(1)

    return token


async def _create_client_instance():
    # New python API update requires these
    intents = discord.Intents.default()
    intents.message_content = True

    # Create discord bot instance
    return DiscordClient(command_prefix="!", intents=intents, help_command=None)


async def setup_bot():
    # Create discord bot instance
    client = await _create_client_instance()

    # Initialise cog system
    cog_system = CogSystem(client)

    # Register all cogs to client
    await cog_system.reg_cogs()

    # Return client so the .start() can be ran
    return client
