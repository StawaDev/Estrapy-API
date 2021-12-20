<h1 align="center">
    Estrapy-API
</h1>

<h2 align="center">
    A Basic Wrapper Anime Image API Created By Stawa
</h2>
<p align="center">
<a href="https://pypi.org/project/Estrapy-API/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/Estrapy-API?style=for-the-badge"></a>
<a href="https://pypi.org/project/Estrapy-API/"><img alt="PyPI" src="https://img.shields.io/pypi/v/Estrapy-API?color=a&label=Estrapy-API&style=for-the-badge"></a>
</p>

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

def function():
    print(f"A Running GIF: {Estrapy.Sfw.run()}")
    print(f"A Hug GIF: {Estrapy.Sfw.hug()}")

function()

# Second Examples
import Estrapy

print(Estrapy.Sfw.run())
print(f"Run: {Estrapy.Sfw.run()}")

# Discord Examples
import Estrapy

@bot.command()
async def run(ctx): # Without Embed
    await ctx.send(Estrapy.Sfw.run())

@bot.command()
async def run(ctx): # With Embed
    embed = discord.Embed(title="Running GIF")
    embed.set_image(url=Estrapy.Sfw.run())
    await ctx.send(embed=embed)
```

### AutoUpdate Estrapy-API

This is only optional, the function will be called if version of Estrapy-API is not same with the newewst one.

```py
import Estrapy
from Estrapy import autoupdate

print(Estrapy.__version__) # Print version of Estrapy-API
```

### Print All Function Endpoints

```py
import Estrapy


print(Estrapy.Help.sfw()) # Print all sfw endpoints
print(Estrapy.Help.nsfw()) # Print all nsfw endpoints
print(Estrapy.Help.all()) # Print all sfw, nsfw endpoints in once
```


### SFW Function Endpoints

SFW Function|Examples|Description
--------------|--------------|--------------
Run     |   Estrapy.Sfw.run()   |   Return SFW Run GIFs
Hug     |   Estrapy.Sfw.hug()   |   Return SFW Hug GIFs
Smile   |   Estrapy.Sfw.smile() |   Return SFW Smile GIFs
Neko    |   Estrapy.Sfw.neko()  |   Return SFW Neko GIFs/PNG
Poke    |   Estrapy.Sfw.poke()  |   Return SFW Poke GIFs
Bite    |   Estrapy.Sfw.bite()  |   Return SFW Bite GIFs
Slap    |   Estrapy.Sfw.slap()  |   Return SFW Slap GIFs
Highfive|   Estrapy.Sfw.highfive()  |    Return SFW Highfive GIFs
Headpat |   Estrapy.Sfw.headpat()   |   Return SFW Headpat GIFs

### NSFW Function Endpoints
NSFW Function|Examples|Description
--------------|--------------|--------------
Kill    |   Estrapy.Nsfw.kill() |   Return NSFW Kill GIFs/PNG
Yuri    |   Estrapy.Nsfw.yuri() |   Return NSFW Yuri GIFs/PNG
Yaoi    |   Estrapy.Nsfw.yaoi() |   Return NSFW Yaoi GIFs/PNG

### GAMES Function Endpoints
GAMES Function|Examples|Description
--------------|--------------|--------------
Truth   |   Estrapy.Games.truth()   |   Return GAMES Truth TEXT
Dare    |   Estrapy.Games.dare()    |   Return GAMES Dare TEXT