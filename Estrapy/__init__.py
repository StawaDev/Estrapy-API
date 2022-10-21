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
__version__ = "0.2.7"
__author__ = "Stawa"
__license__ = "MIT"


class EstraClient:
    """
    Client class for Estrapy, which provides access to the Estrapy's functions.
    """

    __slots__ = (
        "user_id",
        "token_user",
        "Sfw",
        "Nsfw",
        "Games",
        "Help",
        "OsuClient",
        "Trivia",
    )

    def __init__(
        self,
        user_id: Optional[int] = None,
        token_user: Optional[str] = None,
        *args,
        **kwargs
    ):
        self.user_id = user_id
        self.token_user = token_user
        self.Sfw = Sfw(user_id=self.user_id, token_user=self.token_user)
        self.Nsfw = Nsfw(user_id=self.user_id, token_user=self.token_user)
        self.Games = Games(user_id=self.user_id, token_user=self.token_user)
        self.AniGames = AniGames(user_id=self.user_id, token_user=self.token_user)
        self.Help = Help()
        self.OsuClient = OsuClient(
            client_id=kwargs.get("client_id"), client_secret=kwargs.get("client_secret")
        )
        self.Trivia = Trivia()
