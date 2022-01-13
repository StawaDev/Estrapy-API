import Estrapy
import asyncio


# Print All Nsfw Endpoints
async def Help():
    print(await Estrapy.Help.nsfw())


asyncio.run(Help())


# Function Examples
async def function():
    print(f"Yaoi: {await Estrapy.Nsfw.yaoi(generate=2)}")
    print(f"Yuri: {await Estrapy.Nsfw.yuri(generate=2)}")


asyncio.run(function())

# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def yaoi(ctx):
    await ctx.send(await Estrapy.Nsfw.yaoi())


@bot.command()
async def dare(ctx):
    await ctx.send(await Estrapy.Nsfw.yuri())


# Discord Examples With Embed
@bot.command()
async def yaoi(ctx):
    embed = discord.Embed(title="Yaoi")
    embed.set_image(await Estrapy.Nsfw.yaoi())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


@bot.command()
async def yuri(ctx):
    embed = discord.Embed(title="Yuri")
    embed.set_image(await Estrapy.Nsfw.yuri())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


bot.run("TOKEN")
