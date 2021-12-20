import Estrapy

# Print All Games Endpoints
print(Estrapy.Help.games())

# Print Only Examples
print(Estrapy.Games.dare())
print(Estrapy.Games.truth())

# Function Examples
def function():
    print(f"Truth: {Estrapy.Games.truth()}")
    print(f"Dare: {Estrapy.Games.dare()}")


function()


# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def truth(ctx):
    await ctx.send(Estrapy.Games.truth())


@bot.command()
async def dare(ctx):
    await ctx.send(Estrapy.Games.dare())


bot.run("TOKEN")
