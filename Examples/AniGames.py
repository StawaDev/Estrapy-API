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


bot.run("TOKEN")
