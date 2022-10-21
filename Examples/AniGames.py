import Estrapy
import asyncio
from Estrapy import EstraClient

AniGames = EstraClient().AniGames

# Print All AniGames Endpoints
async def Help():
    print(Estrapy.Help.anigames())


asyncio.run(Help())

# Function Examples
async def truth_dare():
    truth = await AniGames.truth()
    dare = await AniGames.dare()

    print(f"Truth: {truth.text}")
    print(f"Dare: {dare.text}")


asyncio.run(truth_dare())


# Second Examples
async def waifu_husbando():
    waifu = await AniGames.waifu()
    print(f"Image Link: {waifu.url}, Character Name: {waifu.character_name}")

    husbando = await AniGames.husbando()
    print(f"Image Link: {husbando.url}, Character Name: {husbando.character_name}")


asyncio.run(waifu_husbando())


# Third Examples
async def shipper_player():
    data = await AniGames.shipper_waifu(player="Stawa")
    print(
        f"Player: {data.player}, Character: {data.character_name}, Percentage: {data.percentage}"
    )


asyncio.run(shipper_player())


# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def truth(ctx):
    truth = await AniGames.truth()
    await ctx.send(truth.text)


@bot.command()
async def dare(ctx):
    dare = await AniGames.dare()
    await ctx.send(dare.text)


@bot.command()
async def waifu(ctx):
    waifu = await AniGames.waifu()
    await ctx.send(waifu.url)


@bot.command()
async def husbando(ctx):
    husbando = await AniGames.husbando()
    await ctx.send(husbando.url)


# Embed Version
@bot.command()
async def waifu_embed(ctx):
    waifu = await AniGames.waifu()

    embed = discord.Embed(title=waifu.character_name)
    embed.set_image(waifu.url)
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


@bot.command()
async def husbando_embed(ctx):
    husbando = await AniGames.husbando()

    embed = discord.Embed(title=husbando.character_name)
    embed.set_image(husbando.url)
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


bot.run("TOKEN")
