from Estrapy import EstraClient
import asyncio

# You can get them from https://estra-db.vercel.app
client_id = "client_id"
client_secret = "client_secret"

Estra = EstraClient(client_id=client_id, client_secret=client_secret)


async def main():
    hug = await Estra.Sfw.hug()
    print("Hug GIF: ", hug.url)

    yuri = await Estra.Nsfw.yuri()
    print("Yuri PNG: ", yuri.url)

    dare = await Estra.Games.dare()
    print("Dare: ", dare.text)

    help = Estra.Help.all()
    print("Help: ", help)


asyncio.run(main())


async def track_requests():
    run = await Estra.Sfw.run()
    print("Run GIF:", run.url)
    print("Request with Account:", run.with_account)


asyncio.run(track_requests())
