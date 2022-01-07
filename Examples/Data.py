import Estrapy
import asyncio


# Function Examples
async def function():
    print(f"Total Games Truth: {await Estrapy.Data.totalGames('truth')}")
    print(f"Total AniGames Dare: {await Estrapy.Data.totalAniGames('dare')}")
    print(f"Total Sfw Poke: {await Estrapy.Data.totalSfw('poke')}")
    print(f"Total Nsfw Kill: {await Estrapy.Data.totalNsfw('kill')}")


asyncio.run(function())
