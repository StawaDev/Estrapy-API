from .__init__ import __version__, EstraClient
from .base import Base
from .http import Requester
from tabulate import tabulate
from pprint import pprint
import asyncclick as click
import anyio

base = Base()
requester = Requester()


@click.command()
def menu():
    """
    Return basic information about Estrapy-API.
    """
    text = """
    Author  : @StawaDev
    \nLicense : MIT
    \nGithub  : https://github.com/StawaDev/Estrapy-API
    \nAPI     : https://estra-api.vercel.app
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
    type=click.Choice(["all", "sfw", "nsfw", "games", "anigames", "osu"]),
    multiple=False,
)
def help(category):
    """
    Return a list of endpoints from a given category or a list of all endpoints.
    """

    _help = EstraClient().Help

    if str.lower(category) == "all":
        pprint(_help.all(), indent=4)
    if str.lower(category) == "sfw":
        print(_help.sfw())
    if str.lower(category) == "nsfw":
        print(_help.nsfw())
    if str.lower(category) == "games":
        print(_help.games())
    if str.lower(category) == "anigames":
        print(_help.anigames())
    if str.lower(category) == "osu":
        print(_help.osu())


@click.command()
@click.option(
    "--category",
    "-c",
    help="Category of the image",
    type=click.Choice(["sfw", "nsfw", "anigames"]),
    multiple=False,
    required=True,
)
@click.option(
    "--endpoint", "-e", help="Endpoint of the image", multiple=False, required=True
)
@click.option(
    "--total", "-t", default=1, help="Total requests to download", multiple=False
)
@click.option(
    "--filename", "-f", default=None, help="Name of File for image", multiple=False
)
async def save(category: str, endpoint: str, total: int, filename: str = None):
    """
    It will save an image or images with a specified category, endpoints, and total images.
    """

    x = await base.save(
        category=f"{category}/{endpoint}", total=total, filename=filename
    )
    print(x)


@click.command()
@click.option(
    "--category",
    "-c",
    help="Category from the API",
    type=click.Choice(["sfw", "nsfw", "games", "anigames"]),
    multiple=False,
    required=True,
)
@click.option(
    "--endpoint", "-e", help="Endpoint from the category", multiple=False, required=True
)
@click.option(
    "--total", "-t", default=1, help="Total requests to fetch", multiple=False
)
async def requests(category: str, endpoint: str, total: int):
    """
    A test request to the API with a given category and endpoint.
    """

    route = f"{category}/{endpoint}"
    output = requester.get_api(route)

    if total > 1:
        try:
            output = await base.produce(route=route, total=total)
        except:
            output = await base.produce(route=route, total=total, type="text")

    print(output)


@click.group()
def main():
    pass


main.add_command(menu)
main.add_command(help)
main.add_command(save)
main.add_command(requests)
