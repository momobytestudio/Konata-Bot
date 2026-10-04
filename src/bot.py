import discord
from discord.ext import commands

from config import DISCORD_TOKEN, PREFIX


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents,
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print(f"Prefix: {PREFIX}")


bot.run(DISCORD_TOKEN)