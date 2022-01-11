<h1 align="center">
    Estrapy-API
</h1>

<h2 align="center">
    A Basic Wrapper Anime Image API Created By Stawa
</h2>
<p align="center">
<a href="https://stawa.gitbook.io/estraapi-documentation/"><img src ="https://img.shields.io/badge/Estra--API-Documentation-brightgreen?style=for-the-badge"></a>
<a href="https://pypi.org/project/Estrapy-API/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/Estrapy-API?style=for-the-badge"></a>
<a href="https://pypi.org/project/Estrapy-API/"><img alt="PyPI" src="https://img.shields.io/pypi/v/Estrapy-API?color=a&label=Estrapy-API&style=for-the-badge"></a>
</p>

### Features

- Truth or Dare
- Anime GIFs
- Anime Waifu/Husbando Picture
- OSU API Wrapper
- Async Supports
- User Friendly Code

### Installing Estrapy-API

```
pip install estrapy-api
```

or If you want to use latest update of Estrapy-API

```py
pip install git+https://github.com/StawaDev/Estrapy-API
```

### Example to use Estrapy-API

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

### AutoUpdate Estrapy-API

This is only optional, the function will be called if version of Estrapy-API is not same with the newewst one.

```py
import Estrapy
from Estrapy import autoupdate

print(Estrapy.__version__) # Print current version of Estrapy-API
```

### Print All Function Endpoints

```py
import Estrapy
import asyncio

async def Help():
    print(await Estrapy.Help.sfw()) # Print all sfw endpoints
    print(await Estrapy.Help.nsfw()) # Print all nsfw endpoints
    print(await Estrapy.Help.all()) # Print all sfw, nsfw endpoints in once

asyncio.run(Help())
```

### Sfw Function Endpoints

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

### Nsfw Function Endpoints

| NSFW Function | Examples            | Description                  |
| ------------- | ------------------- | ---------------------------- |
| Kill          | Estrapy.Nsfw.kill() | Return Nsfw Kill as GIFs/PNG |
| Yuri          | Estrapy.Nsfw.yuri() | Return Nsfw Yuri as GIFs/PNG |
| Yaoi          | Estrapy.Nsfw.yaoi() | Return Nsfw Yaoi as GIFs/PNG |

### AniGames Function Endpoints

| AniGames Function | Examples                    | Description                                  |
| ----------------- | --------------------------- | -------------------------------------------- |
| Truth             | Estrapy.AniGames.truth()    | Return AniGames Truth About Anime as Text    |
| Dare              | Estrapy.AniGames.dare()     | Return AniGames Dare About Anime as Text     |
| Waifu             | Estrapy.AniGames.waifu()    | Return AniGames Waifu About Anime as PNG     |
| Husbando          | Estrapy.AniGames.husbando() | Return AniGames Husbando About Anime as Text |

### Games Function Endpoints

| Games Function | Examples              | Description                |
| -------------- | --------------------- | -------------------------- |
| Truth          | Estrapy.Games.truth() | Return Games Truth as Text |
| Dare           | Estrapy.Games.dare()  | Return Games Dare as Text  |

### OsuClients Function Endpoints

| OsuClients Function | Examples                                                              | Description                 |
| ------------------- | --------------------------------------------------------------------- | --------------------------- |
| OsuProfile          | Estrapy.OsuClients.osuprofile("username", client_id, client_secret)   | Return OsuProfile JSON Data |
| OsuBeatmap          | Estrapy.OsuClients.osubeatmap("beatmap_id", client_id, client_secret) | Return OsuBeatmap JSON Data |
| More Examples       | [In Our Github!](https://github.com/StawaDev/Estrapy-API)             | More examples I guess?      |

### Links

- [Documentation](https://stawa.gitbook.io/estraapi-documentation)
- [Homepage](https://github.com/StawaDev/EstraDart)
- [Application Programming Interface](https://estra-api.herokuapp.com)
