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
Run     |   Estrapy.Sfw.run()   |   Return SFW Run GIF
Hug     |   Estrapy.Sfw.hug()   |   Return SFW Hug GIF
Smile   |   Estrapy.Sfw.smile() |   Return SFW Smile GIF
Neko    |   Estrapy.Sfw.neko()  |   Return SFW Neko GIF/PNG
Poke    |   Estrapy.Sfw.poke()  |   Return SFW Poke GIF
Bite    |   Estrapy.Sfw.bite()  |   Return SFW Bite GIF
Headpat |   Estrapy.Sfw.headpat()   |   Return SFW Headpat GIF

### NSFW Function Endpoints
NSFW Function|Examples|Description
--------------|--------------|--------------
Kill    |   Estrapy.Nsfw.kill() |   Return NSFW Kill GIF/PNG
Yuri    |   Estrapy.Nsfw.yuri() |   Return NSFW Yuri GIF/PNG
Yaoi    |   Estrapy.Nsfw.yaoi() |   Return NSFW Yaoi GIF/PNG
