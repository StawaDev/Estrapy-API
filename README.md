<h1 align="center">
    Estrapy-API
</h1>

<h2 align="center">
    A Basic Anime Image API Created By Stawa
</h2>

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
print(f"Run: {Estrapy.sfw.run()})
```

### SFW Function Endpoints

SFW Function|Examples|Description
--------------|--------------|--------------
Run     |    Estrapy.sfw.run()  | Return SFW Run GIF
Hug     |   Estrapy.sfw.hug()   | Return SFW Hug GIF
Smile   |  Estrapy.sfw.smile()  | Return SFW Smile GIF
Headpat |   Estrapy.sfw.headpat()   | Return SFW Headpat GIF

### NSFW Function Endpoints
NSFW Function|Examples|Description
--------------|--------------|--------------
Coming Soon!     |    Coming Soon!  | Coming Soon!