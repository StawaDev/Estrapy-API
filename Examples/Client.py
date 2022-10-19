from Estrapy import EstraClient
import asyncio

Estra = EstraClient()

# You can get them from https://estra-db.vercel.app
Estra.token_user = "MyUserToken"
Estra.user_id = "MyUserID"


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


async def track_requests():
    run = await Estra.Sfw.run(Estra)
    print("Run GIF:", run.url)
    print("Request with Account:", run.with_account)


asyncio.run(track_requests())
