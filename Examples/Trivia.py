import asyncio
from Estrapy import Trivia

EstraTrivia = Trivia()


async def console():
    await EstraTrivia.run_console()


asyncio.run(console())

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def trivia(ctx):
    question = await EstraTrivia.run(random_pick=True)
    await ctx.send("Question: {}\n{}".format(question[0], ' '.join(question[3])))
    answer = await bot.wait_for(
        "message", check=lambda message: message.author == ctx.author
    )
    check = await EstraTrivia.answer(question, str(answer.content))

    if check[0] is True:
        return await ctx.send("Correct!")
    await ctx.send("Incorrect!")

bot.run("TOKEN")
