import Estrapy
import asyncio
from Estrapy import EstraClient

Games = EstraClient().Games

# Print All Games Endpoints
async def Help():
    print(Estrapy.Help.games())


asyncio.run(Help())


# Function Examples
async def truth_dare():
    truth = await Games.truth()
    dare = await Games.dare()

    print(f"Truth: {truth.text}")
    print(f"Dare: {dare.text}")


asyncio.run(truth_dare())


# Shipper Examples
async def shipper():
    _player = {
        "player_1": "User_1",
        "player_2": "User_2",
    }

    _background = {
        "background_url": "https://xxx",
        "background_size": "1920x720",
    }

    x = await Games.shipper(players=_player, background=_background)
    x.save("Shipper.png")


asyncio.run(shipper())


# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def truth(ctx):
    truth = await Games.truth()
    await ctx.send(truth.text)


@bot.command()
async def dare(ctx):
    dare = await Games.dare()
    await ctx.send(dare.text)


bot.run("TOKEN")
