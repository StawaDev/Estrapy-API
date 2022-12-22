import asyncio
from Estrapy import Trivia

EstraTrivia = Trivia(
    path="Data/questions.json"
)  # The user can now change the names of folders and files.


async def create_question():
    options = {"A": "Stawa", "B": "RandomPerson", "C": "Phone"}

    question = await EstraTrivia.add(
        question="Who is the creator of this packages?",
        answer="A",  # Or list(options)[0]
        options=options,
    )
    print(question)


asyncio.run(create_question())


async def remove_question():
    print(await EstraTrivia.remove(1))  # Remove question number 1


asyncio.run(remove_question())


async def console():
    await EstraTrivia.run_console()


asyncio.run(console())

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def trivia(ctx):
    num, question, answer, options = await EstraTrivia.run(random_pick=True)
    await ctx.send(f"Question ({num}): {question}\n{options}")
    answer = await bot.wait_for(
        "message", check=lambda message: message.author == ctx.author
    )
    check = await EstraTrivia.answer(question, str(answer.content))

    if check[0] is True:
        return await ctx.send("Correct!")
    await ctx.send("Incorrect!")


bot.run("TOKEN")
