from Estrapy import EstraClient
import asyncio

Estra = EstraClient()


async def main():
    hug = await Estra.Sfw.hug()
    print("Hug GIF: ", hug.url)

    yuri = await Estra.Nsfw.yuri()
    print("Yuri PNG: ", yuri.url)

    dare = await Estra.Games.dare()
    print("Dare: ", dare.text)

    help = await Estra.Help.all()
    print("Help: ", help)


asyncio.run(main())
