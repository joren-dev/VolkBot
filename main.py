import asyncio
import discord

from src.globals.client_instance import DiscordClient

# Setup bot and initialise singleton
intents = discord.Intents.default()
intents.message_content = True
DiscordClient(command_prefix="!", intents=intents, help_command=None)


# Imported after to ensure DiscordClient() isnt called before initial initialization.
from src.utils.small_utility import get_env_token
from src.managers.event_manager import EventManager
from src.managers.cog_system import CogSystem


async def main():
    # Initialise event manager
    EventManager()

    # Initialise cog system
    cog_system = CogSystem(DiscordClient())

    # Register all cogs to client
    await cog_system.reg_cogs()

    # Get token from .env and start up bot accordingly
    await DiscordClient().start(get_env_token("TOKEN"))


if __name__ == "__main__":
    asyncio.run(main())
