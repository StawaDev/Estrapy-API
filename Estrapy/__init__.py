from .sfw import *
from .nsfw import *
from .games import *
from .osu import *
from .trivia import *
from .autoupdate import *
from .errors import *
from .help import Help

__title__ = "Estrapy-API"
__version__ = "0.2.7"
__author__ = "Stawa"
__license__ = "MIT"


class EstraClient:
    """
    Client class for Estrapy, which provides access to the Estrapy's functions.
    """

    def __init__(self, *args, **kwargs):
        self.Sfw = Sfw()
        self.Nsfw = Nsfw()
        self.Games = Games()
        self.Help = Help()
        self.OsuClient = OsuClient(
            client_id=kwargs.get("client_id"), client_secret=kwargs.get("client_secret")
        )
        self.Trivia = Trivia()
