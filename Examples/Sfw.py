import Estrapy

# Print All Sfw Endpoints
print(Estrapy.Help.sfw())

# Print Only Examples

print(Estrapy.Sfw.neko())
print(Estrapy.Sfw.hug())


# Function Examples
def function():
    print(f"Smile: {Estrapy.Nsfw.smile()}")
    print(f"Poke: {Estrapy.Nsfw.poke()}")


function()

# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def highfive(ctx):
    await ctx.send(Estrapy.Sfw.highfive())


@bot.command()
async def headpat(ctx):
    await ctx.send(Estrapy.Sfw.headpat())


# Discord Examples With Embed
@bot.command()
async def bite(ctx):
    embed = discord.Embed(title="Bite")
    embed.set_image(Estrapy.Sfw.bite())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


@bot.command()
async def slap(ctx):
    embed = discord.Embed(title="Slap")
    embed.set_image(Estrapy.Sfw.slap())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


bot.run("TOKEN")
