import Estrapy
import asyncio


# Print All AniGames Endpoints
async def Help():
    print(await Estrapy.Help.anigames())


asyncio.run(Help())

# Function Examples
async def function():
    print(f"Truth: {await Estrapy.AniGames.truth()}")
    print(f"Dare: {await Estrapy.AniGames.dare()}")


asyncio.run(function())


# Second Examples
async def function2():
    data = await Estrapy.AniGames.waifu()
    print(f"Image Link: {data['link']}, Character Name: {data['character_name']}")

    data2 = await Estrapy.AniGames.husbando()
    print(f"Image Link: {data2['link']}, Character Name: {data2['character_name']}")


asyncio.run(function2())


# Third Examples
async def function3():
    data = await Estrapy.AniGames.shipper_waifu(player="Stawa")
    print(
        f"Player: {data['player']}, Character: {data['character']}, Percentage: {data['percentage']}"
    )


asyncio.run(function3())


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
