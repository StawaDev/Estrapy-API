import Estrapy
from Estrapy import OsuClients
import asyncio

client_id = ""  # Put your own osu client_id
client_secret = ""  # Put your own osu client_secret
Osu = OsuClients(client_id=client_id, client_secret=client_secret)
OsuObject = OsuClients(
    client_id=client_id, client_secret=client_secret, output="object"
)


async def beatmap():
    data = await Osu.osubeatmap(beatmap_id="2405223")
    data_formatter = await Osu.osubeatmap(
        beatmap_id="2405223",
        formatter=True,  # Keep it on mind, this will only making the output with better formatting JSON format
    )
    print(data["beatmapset"]["artist"])
    print(data_formatter)


asyncio.run(beatmap())


async def profile():
    data = await Osu.osuprofile(username="Stawa")
    data_formatter = await Osu.osuprofile(
        username="Stawa",
        formatter=True,  # Keep it on mind, this will only making the output with better formatting JSON format
    )
    print(data["country"]["name"])
    print(data_formatter)


asyncio.run(profile())


async def osu_object():
    example = await OsuObject.osuprofile(username="Stawa")
    print(example.avatar_url)
    print(example.discord)


asyncio.run(osu_object())
