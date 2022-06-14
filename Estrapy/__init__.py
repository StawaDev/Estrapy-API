from .sfw import *
from .nsfw import *
from .games import *
from .data import *
from .autoupdate import *
from .errors import *
from .help import Help

__title__ = "Estrapy-API"
__version__ = "0.2.4"
__author__ = "Stawa"
__license__ = "MIT"


class EstraClient:
    """
    Client class for Estrapy-API, which provides access to the Estrapy-API's functions.
    """

    def __init__(self):
        self.Sfw = Sfw()
        self.Nsfw = Nsfw()
        self.Games = Games()
        self.Help = Help()
