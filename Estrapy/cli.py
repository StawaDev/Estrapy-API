from .help import Help
from .__init__ import __version__
from .http import get_api
from tabulate import tabulate
import asyncclick as click
import anyio
import requests


@click.command()
async def menu():
    """
    Information about Estrapy-API
    """
    text = """
    Author  : @StawaDev
    \nLicense : MIT
    \nGithub  : https://github.com/StawaDev/Estrapy-API
    \nAPI     : https://estra-api.herokuapp.com/api/
    """
    output = tabulate(
        [[text]],
        tablefmt="fancy_grid",
        headers=["Estrapy-API - v{}".format(__version__)],
        numalign="center",
    )
    print(output)


@click.command()
@click.option(
    "--category",
    "-c",
    default="all",
    help="Show specific categories with endpoints | --category <category>",
    type=click.Choice(["all", "sfw", "nsfw", "games", "anigames"]),
    multiple=False,
)
async def help(category):
    """
    A Help Function for Estrapy Using Command Line Interface.
    """
    if str.lower(category) == "all":
        print(await Help.all())
    if str.lower(category) == "sfw":
        print(await Help.sfw())
    if str.lower(category) == "nsfw":
        print(await Help.nsfw())
    if str.lower(category) == "games":
        print(await Help.games())
    if str.lower(category) == "anigames":
        print(await Help.anigames())


@click.command()
@click.option(
    "--category",
    "-c",
    default="sfw",
    help="Category of the image",
    type=click.Choice(["sfw", "nsfw", "games", "anigames"]),
    multiple=False,
)
@click.option(
    "--endpoint", "-e", default="hug", help="Endpoint of the image", multiple=False
)
async def save(category, endpoint):
    """
    A Save Function for Estrapy Using Command Line Interface.
    """
    try:
        x = get_api(f"{category}/{endpoint}")
        with open(f"{endpoint}.{x['type']}", "wb") as f:
            f.write(requests.get(x["link"]).content)
            print(f"{endpoint}.{x['type']} saved!")
    except:
        print("Error! Please check your endpoint and category.")


@click.group()
def main():
    pass


main.add_command(menu)
main.add_command(help)
main.add_command(save)
