from Estrapy import EstraClient
import asyncio

Estra = EstraClient()


async def main():
    print("Hug GIF: ", await Estra.Sfw.hug())
    print("Yuri PNG: ", await Estra.Nsfw.yuri())
    print("Dare: ", await Estra.Games.dare())
    print("Help: ", await Estra.Help.all())


asyncio.run(main())
