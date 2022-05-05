import Estrapy
import asyncio

# Print All Sfw Endpoints
async def Help():
    print(await Estrapy.Help.sfw())


asyncio.run(Help())


# Function Examples
async def function():
    print(f"Smile: {await Estrapy.Sfw.smile(generate=2)}")
    print(f"Poke: {await Estrapy.Sfw.poke(generate=2)}")


asyncio.run(function())

# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def highfive(ctx):
    await ctx.send(await Estrapy.Sfw.highfive())


@bot.command()
async def headpat(ctx):
    await ctx.send(await Estrapy.Sfw.headpat())


# Discord Examples With Embed
@bot.command()
async def bite(ctx):
    embed = discord.Embed(title="Bite")
    embed.set_image(await Estrapy.Sfw.bite())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


@bot.command()
async def slap(ctx):
    embed = discord.Embed(title="Slap")
    embed.set_image(await Estrapy.Sfw.slap())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


bot.run("TOKEN")
