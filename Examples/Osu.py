import Estrapy
from Estrapy import OsuClient, EstraClient
import asyncio

client_id = "xxx"  # Put your own osu client_id
client_secret = "xxx"  # Put your own osu client_secret
Osu = OsuClient(client_id=client_id, client_secret=client_secret)

# With Maintain Track of Requests
# token_user = ""
# user_id = 123
# Osu = EstraClient(
#    token_user=token_user,
#    user_id=user_id,
#    client_id=client_id,
#    client_secret=client_secret,
# ).OsuClient


async def beatmap():
    data = await Osu.beatmap(beatmap_id=2405223)
    print(data.beatmapset.get("artist"))


asyncio.run(beatmap())


async def profile():
    data = await Osu.profile(username="Stawa")
    print(data.country.get("name"))


asyncio.run(profile())
