import asyncio

import discord
from discord.ext import commands

from config import DISCORD_TOKEN, PREFIX


intents = discord.Intents.default()
intents.message_content = True


class KonataBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            intents=intents,
        )

    async def setup_hook(self):
        # Cogs will be loaded here as we add them.
        pass


bot = KonataBot()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print(f"Prefix: {PREFIX}")


async def main():
    async with bot:
        await bot.start(DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())