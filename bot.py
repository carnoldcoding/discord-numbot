import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import tasks
from datetime import time
import pytz

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

CHANNEL_ID = 1462682536210727058  

intents = discord.Intents.default()
client = discord.Client(intents=intents)

TIMEZONE = pytz.timezone("US/Eastern") 

@tasks.loop(time=time(hour=0, minute=0, tzinfo=TIMEZONE))
async def daily_number():
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        channel = await client.fetch_channel(CHANNEL_ID)

    number = random.randint(0, 9)
    await channel.send(str(number))

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    if not daily_number.is_running():
        daily_number.start()

client.run(TOKEN)
