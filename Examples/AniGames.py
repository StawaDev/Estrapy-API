import Estrapy

# Print All AniGames Endpoints
print(Estrapy.Help.anigames())

# Print Only Examples
print(Estrapy.AniGames.dare())
print(Estrapy.AniGames.truth())

# Function Examples
def function():
    print(f"Truth: {Estrapy.AniGames.truth()}")
    print(f"Dare: {Estrapy.AniGames.dare()}")
    print(f"Waifu: {Estrapy.AniGames.waifu()}")
    print(f"Husbando: {Estrapy.AniGames.husbando()}")


function()


# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def truth(ctx):
    await ctx.send(Estrapy.AniGames.truth())


@bot.command()
async def dare(ctx):
    await ctx.send(Estrapy.AniGames.dare())

@bot.command()
async def waifu(ctx):
    await ctx.send(Estrapy.AniGames.waifu())
    
@bot.command()
async def husbando(ctx):
    await ctx.send(Estrapy.AniGames.husbando())

# Embed Version
@bot.command()
async def waifu(ctx):
    embed = discord.Embed(title="Waifu")
    embed.set_image(Estrapy.Sfw.waifu())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)
    
@bot.command()
async def husbando(ctx):
    embed = discord.Embed(title="Husbando")
    embed.set_image(Estrapy.Sfw.husbando())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)   

bot.run("TOKEN")
