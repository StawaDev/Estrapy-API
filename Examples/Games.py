import Estrapy
import asyncio


# Print All Games Endpoints
async def Help():
    print(await Estrapy.Help.games())


asyncio.run(Help())


# Function Examples
async def truth_dare():
    truth = await Estrapy.Games.truth()
    dare = await Estrapy.Games.dare()

    print(f"Truth: {truth.text}")
    print(f"Dare: {dare.text}")


asyncio.run(truth_dare())


# Shipper Examples
async def shipper():
    test = await Estrapy.Games.shipper(
        player="Player1",
        player2="Player2",
        player_image="None",
        player2_image="None",
        background="None",
        background_size="None",
    )
    test.show()  # Showing the Image
    test.save("Shipper.png")  # Saving the Image


asyncio.run(shipper())


# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def truth(ctx):
    truth = await Estrapy.Games.truth()
    await ctx.send(truth.text)


@bot.command()
async def dare(ctx):
    dare = await Estrapy.Games.dare()
    await ctx.send(dare.text)


bot.run("TOKEN")
