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
    print(f"A Running GIF: {Estrapy.sfw.run()}")
    print(f"A Hug GIF: {Estrapy.sfw.hug()}")

function()

# Second Examples
import Estrapy

print(Estrapy.sfw.run())
print(f"Run: {Estrapy.sfw.run()}")
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


print(Estrapy.EstraHelp.sfw()) # Print all sfw endpoints
print(Estrapy.EstraHelp.nsfw()) # Print all nsfw endpoints
print(Estrapy.EstraHelp.all()) # Print all sfw, nsfw endpoints in once
```


### SFW Function Endpoints

SFW Function|Examples|Description
--------------|--------------|--------------
Run     |   Estrapy.sfw.run()   |   Return SFW Run GIF
Hug     |   Estrapy.sfw.hug()   |   Return SFW Hug GIF
Smile   |   Estrapy.sfw.smile() |   Return SFW Smile GIF
Neko    |   Estrapy.sfw.neko()  |   Return SFW Neko GIF
Poke    |   Estrapy.sfw.poke()  |   Return SFW Poke GIF
Bite    |   Estrapy.sfw.bite()  |   Return SFW Bite GIF
Headpat |   Estrapy.sfw.headpat()   |   Return SFW Headpat GIF

### NSFW Function Endpoints
NSFW Function|Examples|Description
--------------|--------------|--------------
Kill    |   Estrapy.nsfw.kill() |   Return NSFW Kill GIF
Yuri    |   Estrapy.nsfw.yuri() |   Return NSFW Yuri GIF
Yaoi    |   Estrapy.nsfw.yaoi() |   Return NSFW Yaoi GIF