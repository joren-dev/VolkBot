import asyncio

from src.utils.small_utility import get_env_token, setup_bot


async def main():
    client = await setup_bot()

    # Get token from .env and start up bot accordingly
    await client.start(get_env_token("TOKEN"))

if __name__ == '__main__':
    asyncio.run(main())
