from .__init__ import __version__
from .help import Help
from .base import Base
from tabulate import tabulate
import asyncclick as click
import anyio


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
        print(Base.json_beautifier(await Help.all()))
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
    type=click.Choice(["sfw", "nsfw", "anigames"]),
    multiple=False,
)
@click.option(
    "--endpoint", "-e", default="hug", help="Endpoint of the image", multiple=False
)
@click.option(
    "--total", "-t", default=1, help="Total requests to download", multiple=False
)
@click.option(
    "--filename", "-f", default=None, help="Name of File for image", multiple=False
)
async def save(category: str, endpoint: str, total: int, filename: str = None):
    """
    A Save Function for Estrapy Using Command Line Interface.
    """

    x = await Base.save(
        category=f"{category}/{endpoint}", total=total, filename=filename
    )
    print(x)


@click.group()
def main():
    pass


main.add_command(menu)
main.add_command(help)
main.add_command(save)
