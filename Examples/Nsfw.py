import Estrapy

# Print All Nsfw Endpoints
print(Estrapy.Help.nsfw())

# Print Only Examples

print(Estrapy.Nsfw.yaoi())
print(Estrapy.Nsfw.yuri())


# Function Examples
def function():
    print(f"Yaoi: {Estrapy.Nsfw.yaoi()}")
    print(f"Yuri: {Estrapy.Nsfw.yuri()}")


function()

# Discord Examples

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def yaoi(ctx):
    await ctx.send(Estrapy.Nsfw.yaoi())


@bot.command()
async def dare(ctx):
    await ctx.send(Estrapy.Nsfw.yuri())


# Discord Examples With Embed
@bot.command()
async def yaoi(ctx):
    embed = discord.Embed(title="Yaoi")
    embed.set_image(Estrapy.Nsfw.yaoi())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


@bot.command()
async def yuri(ctx):
    embed = discord.Embed(title="Yuri")
    embed.set_image(Estrapy.Nsfw.yuri())
    embed.set_footer(text="Powered by Estrapy")
    await ctx.send(embed=embed)


bot.run("TOKEN")
