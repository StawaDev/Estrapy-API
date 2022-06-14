<h1 align="center">
    Estrapy-API
</h1>

<h2 align="center">
    A Basic Wrapper Anime Image API with Many Features
</h2>
<p align="center">
<a href="https://stawa.gitbook.io/estraapi-documentation/"><img src ="https://img.shields.io/badge/Estra--API-Documentation-brightgreen?style=for-the-badge"></a>
<a href="https://pypi.org/project/Estrapy-API/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/Estrapy-API?style=for-the-badge"></a>
<a href="https://pypi.org/project/Estrapy-API/"><img alt="PyPI" src="https://img.shields.io/pypi/v/Estrapy-API?color=a&label=Estrapy-API&style=for-the-badge"></a>
</p>

### :sparkles: Features

- Async Supports
- Anime GIFs
- Anime Waifu/Husbando Picture
- Client Supports
- User Friendly Code
- OSU API Wrapper
- Trivia
- Truth or Dare

### 📦 Installing The Stable Version of Estrapy-API

```
pip install estrapy-api
```

### 🚧 Installing The Latest Version of Estrapy-API

```py
pip install git+https://github.com/StawaDev/Estrapy-API
```

### :open_book: Example to use Estrapy-API

```py
# First Examples
import Estrapy
import asyncio

async def function():
    print(f"A Running GIF: {await Estrapy.Sfw.run()}")
    print(f"A Hug GIF: {await Estrapy.Sfw.hug()}")

asyncio.run(function())


# Discord Examples
import Estrapy

@bot.command()
async def run(ctx): # Without Embed
    await ctx.send(await Estrapy.Sfw.run())

@bot.command()
async def run(ctx): # With Embed
    embed = discord.Embed(title="Running GIF")
    embed.set_image(url=await Estrapy.Sfw.run())
    await ctx.send(embed=embed)
```

### :bookmark: Automatically Updating Estrapy-API

This is only optional, the function will be called if version of Estrapy-API is not same with the newewst one.

```py
import Estrapy
from Estrapy import AutoUpdate

EstraUpdate = AutoUpdate(reminder=True, auto=False).run()

print(Estrapy.__version__) # Print current version of Estrapy-API
```

### :grey_question: Help Functions for Estrapy-API

```py
import Estrapy
import asyncio

async def Help():
    print(await Estrapy.Help.sfw()) # Print all sfw endpoints
    print(await Estrapy.Help.nsfw()) # Print all nsfw endpoints
    print(await Estrapy.Help.all()) # Print all sfw, nsfw endpoints in once

asyncio.run(Help())
```

### :desktop_computer: Console Input Examples

```s
1. estrapy --help # Output all available commands
2. estrapy menu # Output information about Estrapy-API
3. estrapy help --category <category> # Output all available endpoints in <category>
4. estrapy save --category <category> --endpoint <endpoint> # Save an Image from EstraAPI (with specific category and endpoint) to your computer
```

### :ok_hand: Sfw Function Endpoints

| Sfw Function | Examples               | Description                 |
| ------------ | ---------------------- | --------------------------- |
| Run          | Estrapy.Sfw.run()      | Return Sfw Run as GIFs      |
| Hug          | Estrapy.Sfw.hug()      | Return Sfw Hug as GIFs      |
| Smile        | Estrapy.Sfw.smile()    | Return Sfw Smile as GIFs    |
| Neko         | Estrapy.Sfw.neko()     | Return Sfw Neko as GIFs/PNG |
| Poke         | Estrapy.Sfw.poke()     | Return Sfw Poke as GIFs     |
| Bite         | Estrapy.Sfw.bite()     | Return Sfw Bite as GIFs     |
| Slap         | Estrapy.Sfw.slap()     | Return Sfw Slap as GIFs     |
| Highfive     | Estrapy.Sfw.highfive() | Return Sfw Highfive as GIFs |
| Headpat      | Estrapy.Sfw.headpat()  | Return Sfw Headpat as GIFs  |

### :interrobang: Nsfw Function Endpoints

| NSFW Function | Examples            | Description                  |
| ------------- | ------------------- | ---------------------------- |
| Kill          | Estrapy.Nsfw.kill() | Return Nsfw Kill as GIFs/PNG |
| Yuri          | Estrapy.Nsfw.yuri() | Return Nsfw Yuri as GIFs/PNG |
| Yaoi          | Estrapy.Nsfw.yaoi() | Return Nsfw Yaoi as GIFs/PNG |

### :video_game: AniGames Function Endpoints

| AniGames Function | Examples                    | Description                                  |
| ----------------- | --------------------------- | -------------------------------------------- |
| Truth             | Estrapy.AniGames.truth()    | Return AniGames Truth About Anime as Text    |
| Dare              | Estrapy.AniGames.dare()     | Return AniGames Dare About Anime as Text     |
| Waifu             | Estrapy.AniGames.waifu()    | Return AniGames Waifu About Anime as PNG     |
| Husbando          | Estrapy.AniGames.husbando() | Return AniGames Husbando About Anime as Text |

### :video_game: Games Function Endpoints

| Games Function | Examples                | Description                   |
| -------------- | ----------------------- | ----------------------------- |
| Truth          | Estrapy.Games.truth()   | Return Games Truth as Text    |
| Dare           | Estrapy.Games.dare()    | Return Games Dare as Text     |
| Shipper        | Estrapy.Games.shipper() | Return Games Shipper as Image |

### <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Osu%21_Logo_2016.svg/1024px-Osu%21_Logo_2016.svg.png width="30" height="30"> OsuClients Function Endpoints

| OsuClients Function | Examples                                               | Description                 |
| ------------------- | ------------------------------------------------------ | --------------------------- |
| OsuProfile          | Estrapy.OsuClients.osuprofile(username="username")     | Return OsuProfile JSON Data |
| OsuBeatmap          | Estrapy.OsuClients.osubeatmap(beatmap_id="beatmap_id") | Return OsuBeatmap JSON Data |

### :grey_question: Trivia Function Endpoints

| Trivia Function | Examples                                                                       | Description                          |
| --------------- | ------------------------------------------------------------------------------ | ------------------------------------ |
| Add             | Trivia.add(question="question", answer="answer", options={"option": "option"}) | Add Questions Into A JSON File       |
| Remove          | Trivia.remove(1)                                                               | Removing Question In Specific Number |
| Run_Console     | Trivia.run_console                                                             | Run Trivia Through Console           |
| Run             | Trivia.run(random_pick=True)                                                   | Run Trivia With Return Statement     |
| Answer          | Trivia.answer(run, guess="answer")                                             | Answer Trivia From Run Function      |
| More Examples   | [In Our Github!](https://github.com/StawaDev/Estrapy-API)                      | More examples I guess?               |

### :link: Links

- [Documentation](https://stawa.gitbook.io/estraapi-documentation)
- [Homepage](https://github.com/StawaDev/Estrapy-API)
- [Application Programming Interface](https://estra-api.herokuapp.com)
