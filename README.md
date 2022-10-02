<h1 align="center">
    Estrapy-API
</h1>

<h2 align="center">
    An Easy-to-Use Wrapper Anime Images API with Many Others Features
</h2>
<p align="center">
<a href="https://codeclimate.com/github/StawaDev/Estrapy-API/maintainability"><img src="https://api.codeclimate.com/v1/badges/94df604d6f4f73999c8e/maintainability"/></a>
<a href="https://stawa.gitbook.io/estraapi-documentation/"><img src ="https://img.shields.io/badge/Estra--API-Documentation-brightgreen?style=for-the-badge"></a>
<a href="https://pypi.org/project/Estrapy-API/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/Estrapy-API?style=for-the-badge"></a>
<a href="https://pypi.org/project/Estrapy-API/"><img alt="PyPI" src="https://img.shields.io/pypi/v/Estrapy-API?color=a&label=Estrapy-API&style=for-the-badge"></a>
</p>

### <span class="emoji">✨</span> Features

- Async Supports
- Anime GIFs
- Anime Waifu/Husbando Picture
- Client Supports
- User Friendly Code
- OSU API Wrapper
- Trivia
- Truth or Dare Challenges

### <span class="emoji">📦</span> Installing The Stable Version of Estrapy-API

```
pip install estrapy-api
```

### <span class="emoji">🚧</span> Installing The Latest Version of Estrapy-API

```py
pip install git+https://github.com/StawaDev/Estrapy-API
```

### <span class="emoji">📖</span> Short Example to use Estrapy-API

```py
import Estrapy
import asyncio

async def function():
    run = await Estrapy.Sfw.run()
    hug = await Estrapy.Sfw.hug()

    print(f"A Running GIF: {run.url}")
    print(f"A Hug GIF: {hug.url}")

asyncio.run(function())
```

### <span class="emoji">🔖</span> Automatically Updating Estrapy-API

This is only optional, the function will be called if version of Estrapy-API is not same with the newewst one.

```py
import Estrapy
from Estrapy import AutoUpdate

Auto = AutoUpdate()
updater = Auto.update() # Automatically update Estrapy to the newewst version
print(Auto.reminder()) # Reminder of the newewst update

print(Estrapy.__version__) # Print current version of Estrapy-API
```

### <span class="emoji">❔</span> Help Functions for Estrapy-API

```py
import Estrapy
import asyncio

async def Help():
    print(await Estrapy.Help.sfw()) # Print all sfw endpoints
    print(await Estrapy.Help.nsfw()) # Print all nsfw endpoints
    print(await Estrapy.Help.all()) # Print all sfw, nsfw endpoints in once

asyncio.run(Help())
```

### <span class="emoji">🗔</span> Console Input Examples

```s
1. estrapy --help # Output all available commands
2. estrapy menu # Output information about Estrapy-API
3. estrapy help --category <category> # Output all available endpoints in <category>
4. estrapy save --category <category> --endpoint <endpoint> --total <total> --filename <filename> # Save an Image from EstraAPI (with specific category and endpoint) to your computer
```

<details>

   <summary><span class="emoji">📃</span><b> View List Endpoints of Estrapy</b></summary>

<b>Note: Almost every function implemented to `Estrapy` are returning `PropertiesManager`. You can see the examples from here: https://github.com/StawaDev/Estrapy-API/tree/main/Examples</b>

### <span class="emoji">👌</span> Sfw Function Endpoints

Available PropertiesManager - `url`, `type`

| Sfw Function | Examples               | Output                   |
| ------------ | ---------------------- | ------------------------ |
| Run          | Estrapy.Sfw.run()      | Return PropertiesManager |
| Hug          | Estrapy.Sfw.hug()      | Return PropertiesManager |
| Smile        | Estrapy.Sfw.smile()    | Return PropertiesManager |
| Neko         | Estrapy.Sfw.neko()     | Return PropertiesManager |
| Poke         | Estrapy.Sfw.poke()     | Return PropertiesManager |
| Bite         | Estrapy.Sfw.bite()     | Return PropertiesManager |
| Slap         | Estrapy.Sfw.slap()     | Return PropertiesManager |
| Highfive     | Estrapy.Sfw.highfive() | Return PropertiesManager |
| Headpat      | Estrapy.Sfw.headpat()  | Return PropertiesManager |

### <span class="emoji">⁉️</span> Nsfw Function Endpoints

Available PropertiesManager - `url`, `type`

| NSFW Function | Examples            | Output                   |
| ------------- | ------------------- | ------------------------ |
| Kill          | Estrapy.Nsfw.kill() | Return PropertiesManager |
| Yuri          | Estrapy.Nsfw.yuri() | Return PropertiesManager |
| Yaoi          | Estrapy.Nsfw.yaoi() | Return PropertiesManager |

### <span class="emoji">🎮</span> AniGames Function Endpoints

Available PropertiesManager - `url`, `character_name`, `text`, `type`, `player`, `percentage`

| AniGames Function | Examples                    | Output                   |
| ----------------- | --------------------------- | ------------------------ |
| Truth             | Estrapy.AniGames.truth()    | Return PropertiesManager |
| Dare              | Estrapy.AniGames.dare()     | Return PropertiesManager |
| Waifu             | Estrapy.AniGames.waifu()    | Return PropertiesManager |
| Husbando          | Estrapy.AniGames.husbando() | Return PropertiesManager |

### <span class="emoji">🎮</span> Games Function Endpoints

Available PropertiesManager - `text`, `type`

| Games Function | Examples                | Output                   |
| -------------- | ----------------------- | ------------------------ |
| Truth          | Estrapy.Games.truth()   | Return PropertiesManager |
| Dare           | Estrapy.Games.dare()    | Return PropertiesManager |
| Shipper        | Estrapy.Games.shipper() | Return PropertiesManager |

### <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Osu%21_Logo_2016.svg/1024px-Osu%21_Logo_2016.svg.png width="30" height="30"> OsuClients Function Endpoints

| OsuClients Function | Examples                                               | Description                 |
| ------------------- | ------------------------------------------------------ | --------------------------- |
| OsuProfile          | Estrapy.OsuClients.osuprofile(username="username")     | Return OsuProfile JSON Data |
| OsuBeatmap          | Estrapy.OsuClients.osubeatmap(beatmap_id="beatmap_id") | Return OsuBeatmap JSON Data |

### <span class="emoji">❔</span> Trivia Function Endpoints

| Trivia Function | Examples                                                                       | Description                          |
| --------------- | ------------------------------------------------------------------------------ | ------------------------------------ |
| Add             | Trivia.add(question="question", answer="answer", options={"option": "option"}) | Add Questions Into A JSON File       |
| Remove          | Trivia.remove(1)                                                               | Removing Question In Specific Number |
| Run_Console     | Trivia.run_console                                                             | Run Trivia Through Console           |
| Run             | Trivia.run(random_pick=True)                                                   | Run Trivia With Return Statement     |
| Answer          | Trivia.answer(run, guess="answer")                                             | Answer Trivia From Run Function      |
| More Examples   | [In Our Github!](https://github.com/StawaDev/Estrapy-API)                      | More examples I guess?               |

</details>

### <span class="emoji">🔗</span> Links

- [Documentation](https://stawa.gitbook.io/estraapi-documentation)
- [Homepage](https://github.com/StawaDev/Estrapy-API)
- [Application Programming Interface](https://estra-api.vercel.app)
