import Estrapy
import asyncio
from Estrapy import EstraClient

Nsfw = EstraClient().Nsfw

# Print All Nsfw Endpoints
async def Help():
    print(Estrapy.Help.nsfw())


asyncio.run(Help())


# Generate Function Examples
async def generate():
    yaoi = await Nsfw.yaoi(generate=2)
    yuri = await Nsfw.yuri(generate=2)

    print(f"Yaoi: {yaoi.url}")
    print(f"Yuri: {yuri.url}")


asyncio.run(generate())

# Function Examples
async def function():
    kill = await Nsfw.kill()
    print(f"Kill: {kill.url}")


asyncio.run(function())

# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def yaoi(ctx):
    yaoi = await Nsfw.yaoi()
    await ctx.send(yaoi.url)


@bot.command()
async def yuri(ctx):
    yuri = await Nsfw.yuri()
    await ctx.send(yuri.url)


# Discord Examples With Embed
@bot.command()
async def yaoi_embed(ctx):
    yaoi = await Nsfw.yaoi()

    embed = discord.Embed(title="Yaoi")
    embed.set_image(yaoi.url)
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


@bot.command()
async def yuri_embed(ctx):
    yuri = await Nsfw.yuri()

    embed = discord.Embed(title="Yuri")
    embed.set_image(yuri.text)
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


bot.run("TOKEN")
