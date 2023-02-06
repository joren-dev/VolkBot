from src.globals.client_instance import DiscordClient

# List of all available events & the client instance
_discord_client = DiscordClient()


@_discord_client.event
async def on_ready():
    print(f"Logged on as {_discord_client.user}!")


@_discord_client.event
async def on_message(message):
    print(f"Message lol {message.author}: {message.content}")

    # Ensures commands work properly, wont process any commands without it.
    await _discord_client.process_commands(message)
