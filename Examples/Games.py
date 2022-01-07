import Estrapy
import asyncio


# Print All Games Endpoints
async def Help():
    print(Estrapy.Help.games())

asyncio.run(Help())


# Function Examples
async def function():
    print(f"Truth: {await Estrapy.Games.truth()}")
    print(f"Dare: {await Estrapy.Games.dare()}")


asyncio.run(function())


# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def truth(ctx):
    await ctx.send(await Estrapy.Games.truth())


@bot.command()
async def dare(ctx):
    await ctx.send(await Estrapy.Games.dare())


bot.run("TOKEN")
