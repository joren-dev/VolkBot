import discord
import os
from dotenv import load_dotenv


class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")


load_dotenv()
token = os.getenv("TOKEN")
if token is None:
    print("No token was provided in .env, shutting down...")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(token)
