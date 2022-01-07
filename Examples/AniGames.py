import Estrapy
import asyncio


# Print All AniGames Endpoints
async def Help():
    print(Estrapy.Help.anigames())

asyncio.run(Help())

# Function Examples
async def function():
    print(f"Truth: {Estrapy.AniGames.truth()}")
    print(f"Dare: {Estrapy.AniGames.dare()}")
    print(f"Waifu: {Estrapy.AniGames.waifu()}")
    print(f"Waifu Name: {Estrapy.AniGames.waifu_name()}")
    print(f"Husbando: {Estrapy.AniGames.husbando()}")
    print(f"Husbando Name: {Estrapy.AniGames.husbando_name()}")


asyncio.run(function())


# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def truth(ctx):
    await ctx.send(await Estrapy.AniGames.truth())


@bot.command()
async def dare(ctx):
    await ctx.send(await Estrapy.AniGames.dare())

@bot.command()
async def waifu(ctx):
    await ctx.send(await Estrapy.AniGames.waifu())
    
@bot.command()
async def husbando(ctx):
    await ctx.send(await Estrapy.AniGames.husbando())

# Embed Version
@bot.command()
async def waifu(ctx):
    embed = discord.Embed(title="Waifu")
    embed.set_image(await Estrapy.Sfw.waifu())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)
    
@bot.command()
async def husbando(ctx):
    embed = discord.Embed(title="Husbando")
    embed.set_image(await Estrapy.Sfw.husbando())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)   

bot.run("TOKEN")
