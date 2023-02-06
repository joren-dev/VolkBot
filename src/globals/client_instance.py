from discord.ext import commands

from src.utils.singleton import Singleton


# NOTE: Skeleton of the client to ensure only one object of commands.bot is created by utilising a singleton
class DiscordClient(commands.Bot, metaclass=Singleton):
    pass
