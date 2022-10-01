from .sfw import *
from .nsfw import *
from .games import *
from .autoupdate import *
from .errors import *
from .help import Help

__title__ = "Estrapy"
__version__ = "0.2.7"
__author__ = "Stawa"
__license__ = "MIT"


class EstraClient:
    """
    Client class for Estrapy, which provides access to the Estrapy's functions.
    """

    def __init__(self):
        self.Sfw = Sfw()
        self.Nsfw = Nsfw()
        self.Games = Games()
        self.Help = Help()
        self.Trivia = Trivia()
