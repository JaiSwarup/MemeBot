import os
import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')

token = 'MTA5NjM1MDcyMTQ1ODMyMzU1Ng.G_l_in.kftUlgpV8g7C4raDAN7DsT5UyYVElv7huS8-9w'


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    async with bot:
        await load()
        await bot.start(token)


asyncio.run(main())
