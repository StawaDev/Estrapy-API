from .__init__ import __version__, EstraClient
from .base import Base
from .http import Requester
from tabulate import tabulate
from pprint import pprint
import asyncclick as click
import anyio

base = Base()
client = EstraClient()
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

    _help = client.Help
    call = getattr(_help, category)
    pprint(call(), indent=4)


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
            output = await base.produce(route=route, total=total, type="link")
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
