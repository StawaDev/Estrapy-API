import Estrapy
from Estrapy import OsuClients
import asyncio

client_id = ""  # Put your own osu client_id
client_secret = ""  # Put your own osu client_secret
Osu = OsuClients(client_id=client_id, client_secret=client_secret)
Osu.client_data()


async def beatmap():
    data = await Estrapy.OsuClients.osubeatmap(beatmap_id="2405223")
    data_formatter = await Estrapy.OsuClients.osubeatmap(
        beatmap_id="2405223",
        formatter=True,  # Keep it on mind, this will only making the output with better formatting JSON format
    )
    print(data["beatmapset"]["artist"])
    print(data_formatter)


asyncio.run(beatmap())


async def profile():
    data = await Estrapy.OsuClients.osuprofile(username="Stawa")
    data_formatter = await Estrapy.OsuClients.osuprofile(
        username="Stawa",
        formatter=True,  # Keep it on mind, this will only making the output with better formatting JSON format
    )
    print(data["country"]["name"])
    print(data_formatter)


asyncio.run(profile())
