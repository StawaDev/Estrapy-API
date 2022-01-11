import Estrapy
import asyncio

client_id = ""  # Put your own osu client_id
client_secret = ""  # Put your own osu client_secret


async def beatmap():
    data = await Estrapy.OsuClients.osubeatmap("2405223", client_id, client_secret)
    data_formatter = await Estrapy.OsuClients.osubeatmap(
        "2405223",
        client_id,
        client_secret,
        formatter=True,  # Keep it on mind, this will only making the output with better formatting JSON format
    )
    print(data["beatmapset"]["artist"])
    print(data_formatter)


asyncio.run(beatmap())


async def profile():
    data = await Estrapy.OsuClients.osuprofile("Stawa", client_id, client_secret)
    data_formatter = await Estrapy.OsuClients.osuprofile(
        "Stawa",
        client_id,
        client_secret,
        formatter=True,  # Keep it on mind, this will only making the output with better formatting JSON format
    )
    print(data["country"]["name"])
    print(data_formatter)


asyncio.run(profile())
