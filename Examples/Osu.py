import Estrapy
from Estrapy import EstraClient
import asyncio

osu_client_id = "osu_client_id"  # Put your own osu client_id
osu_client_secret = "osu_client_secret"  # Put your own osu client_secret
client = EstraClient(osu_client_id=osu_client_id, osu_client_secret=osu_client_secret)

# With Maintain Track of Requests
# client_id = ""
# client_secret = ""
# osu = EstraClient(
#    client_id=client_id,
#    client_secret=client_secret,
#    osu_client_id=osu_client_id,
#    osu_client_secret=osu_client_secret,
# )


async def beatmap():
    output = await client.OsuClient.beatmap(beatmap_id=2405223)
    print(output.beatmapset.get("artist"))


asyncio.run(beatmap())


async def profile():
    output = await client.OsuClient.profile(username="Stawa")
    print(output.country.get("name"))


asyncio.run(profile())
