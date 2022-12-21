from .account import *
from .sfw import *
from .nsfw import *
from .games import *
from .osu import *
from .trivia import *
from .autoupdate import *
from .errors import *
from .help import Help
from typing import Optional

__title__ = "Estrapy-API"
__version__ = "0.2.8"
__author__ = "Stawa"
__license__ = "MIT"


class EstraClient:
    """
    Client class for Estrapy, which provides access to the Estrapy's functions.
    """

    __slots__ = (
        "client_id",
        "client_secret",
        "osu_client_id",
        "osu_client_secret",
        "path",
        "AccountManager",
        "Sfw",
        "Nsfw",
        "Games",
        "AniGames",
        "Help",
        "OsuClient",
        "Trivia",
    )

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        **kwargs
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.AccountManager = AccountManager(
            client_id=client_id, client_secret=client_secret
        )
        self.Sfw = Sfw(client_id=self.client_id, client_secret=self.client_secret)
        self.Nsfw = Nsfw(client_id=self.client_id, client_secret=self.client_secret)
        self.Games = Games(client_id=self.client_id, client_secret=self.client_secret)
        self.AniGames = AniGames(
            client_id=self.client_id, client_secret=self.client_secret
        )
        self.Help = Help()
        self.OsuClient = OsuClient(
            osu_client_id=kwargs.get("osu_client_id"),
            osu_client_secret=kwargs.get("osu_client_secret"),
        )
        self.Trivia = Trivia(path=kwargs.get("path"))
