import asyncio
from Estrapy.base import Base

base = Base()


async def save():
    url_list, file_list = await base.save(
        category="sfw/slap", total=3, filename="AnimeSlap"
    )
    print(url_list, file_list)

    filename, url = await base.save(category="sfw/hug", total=1, filename="AnimeHug")
    print(filename, url)


asyncio.run(save())
