import asyncio

from src.globals.client_instance import DiscordClient, setup_bot

from src.utils.small_utility import get_env_token


async def main():
    await setup_bot()

    # Get token from .env and start up bot accordingly
    await DiscordClient().start(get_env_token("TOKEN"))


if __name__ == "__main__":
    asyncio.run(main())
