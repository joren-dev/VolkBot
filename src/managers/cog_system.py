import os


class _CogSystemManager:
    def __init__(self, client):
        self.client = client

    async def reg_debug_cogs(self):
        # Remote code execution module for debugging purposes
        await self.client.load_extension("jishaku")

    async def reg_cogs(self):
        # TODO: Ensure this is only loaded in debug mode, not in live
        self.reg_debug_cogs()

        for filename in os.listdir("./src/cogs"):
            if filename.endswith(".py"):
                await self.client.load_extension(f"src.cogs.{filename[:-3]}")


# Typedef for clarity, make sure to import CogSystem
CogSystem = _CogSystemManager
