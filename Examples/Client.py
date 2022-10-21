from Estrapy import EstraClient
import asyncio

# You can get them from https://estra-db.vercel.app
token_user = "MyUserToken"
user_id = "MyUserID"

Estra = EstraClient(token_user=token_user, user_id=user_id)


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
