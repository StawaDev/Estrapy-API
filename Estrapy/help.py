import json
from pygments import highlight, lexers, formatters

__all__ = ("SFW_LIST", "NSFW_LIST", "GAMES_LIST", "ANIGAMES_LIST", "ALL_DICT", "Help")


SFW_LIST = ["hug", "run", "smile", "headpat", "neko", "bite", "highfive", "poke", "slap",]
NSFW_LIST = ["yaoi", "yuri", "kill"]
GAMES_LIST = ["truth", "dare"]
ANIGAMES_LIST = ["truth", "dare"]
ALL_DICT = {
    "SFW": f", ".join(SFW_LIST),
    "NSFW": f", ".join(NSFW_LIST),
    "GAMES_LIST": f", ".join(GAMES_LIST),
    "ANIGAMES_LIST": f", ".join(ANIGAMES_LIST),
}


class Help:
    @staticmethod
    def sfw():
        """
        Description
        --------------
        A Function That Will Return a List of Sfw Endpoints

        How to use sfw help function (Examples)
        ----------------------------

        ```
        Estrapy.Help.sfw() # Keep it as function or it will return function type
        ```
        """
        return SFW_LIST

    @staticmethod
    def nsfw():
        """
        Description
        --------------
        A Function That Will Return a List of Nsfw Endpoints

        How to use nsfw help function (Examples)
        ----------------------------

        ```
        Estrapy.Help.nsfw() # Keep it as function or it will return function type
        ```
        """
        return NSFW_LIST

    @staticmethod
    def games():
        """
        Description
        --------------
        A Function That Will Return a List of Games Endpoints

        How to use games help function (Examples)
        ----------------------------

        ```
        Estrapy.Help.games() # Keep it as function or it will return function type
        ```
        """
        return GAMES_LIST

    @staticmethod
    def games():
        """
        Description
        --------------
        A Function That Will Return a List of AniGames Endpoints

        How to use anigames games help function (Examples)
        ----------------------------

        ```
        Estrapy.Help.anigames() # Keep it as function or it will return function type
        ```
        """
        return GAMES_LIST

    @staticmethod
    def all():
        """
        Description
        --------------
        A Function That Will Return a List of Sfw, Nsfw, Games Endpoints

        How to use all help function (Examples)
        ----------------------------

        ```
        Estrapy.Help.all() # Keep it as function or it will return function type
        ```
        """
        ALL_LIST = json.dumps(ALL_DICT, indent=6, sort_keys=True)
        ALL_LIST_COLOR = highlight(ALL_LIST, lexers.JsonLexer(), formatters.TerminalFormatter())
        return ALL_LIST_COLOR
