import discord
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        # TODO: get rid of colour hex codes, in code.
        embed = (discord.Embed(description="help command hier", color=0xFF0000),)
        embed.set_author(name="Uitleg planles command")

        await ctx.send(embed=embed)

async def setup(client):
    client.add_cog(help(client))
