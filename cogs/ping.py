from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong! {0}'.format(round(self.client.latency, 1)))

async def setup(client):
    await client.add_cog(Ping(client))
