import Estrapy
import asyncio

client_id = "" # Put your own osu client_id
client_secret = "" # Put your own osu client_secret

async def beatmap():
    print(await Estrapy.OsuClients.osubeatmapdata("2405223", client_id, client_secret))
    print(await Estrapy.OsuClients.osubeatmap("2405223", "beatmapset", client_id, client_secret))
    print(await Estrapy.OsuClients.osubeatmap2("2405223", "beatmapset", "title", client_id, client_secret))
    print(await Estrapy.OsuClients.osubeatmap3("2405223", "beatmapset", "covers", "card", client_id, client_secret))


asyncio.run(beatmap())


async def profile():
    print(await Estrapy.OsuClients.osuprofiledata("Stawa", client_id, client_secret))    
    print(await Estrapy.OsuClients.osuprofile("Stawa", "avatar_url", client_id, client_secret))
    print(await Estrapy.OsuClients.osuprofile2("Stawa", "country", "code", client_id, client_secret))
    print(await Estrapy.OsuClients.osuprofile3("Stawa", "statistics", "grade_counts", "sh", client_id, client_secret))
    

asyncio.run(profile())
