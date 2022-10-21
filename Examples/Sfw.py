import Estrapy
import asyncio
from Estrapy import EstraClient

Sfw = EstraClient().Sfw

# Print All Sfw Endpoints
async def Help():
    print(Estrapy.Help.sfw())


asyncio.run(Help())


# Generate Function Examples
async def generate():
    print(f"Smile: {await Sfw.smile(generate=2)}")
    print(f"Poke: {await Sfw.poke(generate=2)}")


asyncio.run(generate())

# Function Examples
async def function():
    neko = await Sfw.neko()
    print(f"Neko: {neko.url}")

    run = await Sfw.run()
    print(f"Run: {run.url}")


asyncio.run(function())

# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def highfive(ctx):
    highfive = await Sfw.highfive()
    await ctx.send(highfive.url)


@bot.command()
async def headpat(ctx):
    headpat = await Sfw.headpat()
    await ctx.send(headpat.url)


# Discord Examples With Embed
@bot.command()
async def bite(ctx):
    bite = await Sfw.bite()

    embed = discord.Embed(title="Bite")
    embed.set_image(bite.url)
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


@bot.command()
async def slap(ctx):
    slap = await Sfw.slap()

    embed = discord.Embed(title="Slap")
    embed.set_image(slap.url)
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


bot.run("TOKEN")
