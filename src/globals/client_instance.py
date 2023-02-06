import discord

from src.managers.event_manager import EventManager
from src.managers.cog_system import CogSystem


async def setup_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    # Initialise discord bot singleton
    DiscordClient(command_prefix="!", intents=intents, help_command=None)

    # Initialise cog system
    cog_system = CogSystem(DiscordClient())

    # Register all cogs to client
    await cog_system.reg_cogs()


# Typedef for clarity, make sure to import DiscordClient
DiscordClient = EventManager
