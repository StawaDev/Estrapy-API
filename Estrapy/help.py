__all__ = ("SFW_LIST", "NSFW_LIST", "GAMES_LIST", "ANIGAMES_LIST", "ALL_DICT", "Help")


SFW_LIST = [
    "hug",
    "run",
    "smile",
    "headpat",
    "neko",
    "bite",
    "highfive",
    "poke",
    "slap",
]
NSFW_LIST = ["yaoi", "yuri", "kill"]
GAMES_LIST = ["truth", "dare", "shipper"]
ANIGAMES_LIST = [
    "truth",
    "dare",
    "waifu",
    "husbando",
    "shipper_waifu",
    "shipper_husbando",
]
TRIVIA_LIST = ["add", "remove", "answer", "run", "run_console"]
OSU_LIST = ["osuprofile", "osubeatmap"]
ALL_DICT = {
    "SFW": f", ".join(SFW_LIST),
    "NSFW": f", ".join(NSFW_LIST),
    "GAMES_LIST": f", ".join(GAMES_LIST),
    "ANIGAMES_LIST": f", ".join(ANIGAMES_LIST),
    "TRIVIA_LIST": f", ".join(TRIVIA_LIST),
    "OSU_LIST": f", ".join(OSU_LIST),
}


class Help:
    @staticmethod
    async def sfw():
        """
        ## Description
        --------------
        This function will return a list of Sfw categories endpoints.

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        async def sfw():
            print(await Estrapy.Help.sfw()) # Keep it as function or it will return function type
        ```

        """
        return SFW_LIST

    @staticmethod
    async def nsfw():
        """
        ## Description
        --------------
        This function will return a list of Nsfw categories endpoints.

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        async def nsfw():
            print(await Estrapy.Help.nsfw()) # Keep it as function or it will return function type
        ```

        """
        return NSFW_LIST

    @staticmethod
    async def games():
        """
        ## Description
        --------------
        This function will return a list of Games categories endpoints.

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        async def games():
            print(await Estrapy.Help.games()) # Keep it as function or it will return function type
        ```

        """
        return GAMES_LIST

    @staticmethod
    async def anigames():
        """
        ## Description
        --------------
        This function will return a list of AniGames categories endpoints.

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        async def anigames():
            print(await Estrapy.Help.anigames()) # Keep it as function or it will return function type
        ```

        """
        return ANIGAMES_LIST

    @staticmethod
    async def osu():
        """
        ## Description
        --------------
        This function will return a list of Osu categories endpoints.

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        async def osu():
            print(await Estrapy.Help.osu()) # Keep it as function or it will return function type
        ```

        """
        return OSU_LIST

    @staticmethod
    async def all():
        """
        Description
        --------------
        This function will return a list of All categories endpoints (Sfw, Nsfw, Games, AniGames).

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        async def all():
            print(await Estrapy.Help.all()) # Keep it as function or it will return function type
        ```

        """
        return ALL_DICT
