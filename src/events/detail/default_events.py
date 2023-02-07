from src.globals.client_instance import DiscordClient

# List of all available events & the client instance
_discord_client = DiscordClient()


@_discord_client.event
async def on_ready():
    from src.managers.event_manager import EventManager

    for each in EventManager.on_ready_events:
        await each.on_ready()


@_discord_client.event
async def on_message(message):
    # Ensures commands work properly, wont process any commands without it.
    await _discord_client.process_commands(message)

    from src.managers.event_manager import EventManager

    for each in EventManager.on_message_events:
        await each.on_message(message)
