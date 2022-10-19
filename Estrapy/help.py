__all__ = ("Help",)


class Help:
    @staticmethod
    def sfw():
        """
        ## Description
        --------------
        This function will return a list of Sfw categories endpoints.

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        def sfw():
            print(Estrapy.Help.sfw()) # Keep it as function or it will return function type
        ```
        """

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

        return SFW_LIST

    @staticmethod
    def nsfw():
        """
        ## Description
        --------------
        This function will return a list of Nsfw categories endpoints.

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        def nsfw():
            print(Estrapy.Help.nsfw()) # Keep it as function or it will return function type
        ```
        """

        NSFW_LIST = ["yaoi", "yuri", "kill"]

        return NSFW_LIST

    @staticmethod
    def games():
        """
        ## Description
        --------------
        This function will return a list of Games categories endpoints.

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        def games():
            print(Estrapy.Help.games()) # Keep it as function or it will return function type
        ```
        """

        GAMES_LIST = ["truth", "dare", "shipper"]

        return GAMES_LIST

    @staticmethod
    def anigames():
        """
        ## Description
        --------------
        This function will return a list of AniGames categories endpoints.

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        def anigames():
            print(Estrapy.Help.anigames()) # Keep it as function or it will return function type
        ```
        """

        ANIGAMES_LIST = [
            "truth",
            "dare",
            "waifu",
            "husbando",
            "shipper_waifu",
            "shipper_husbando",
        ]

        return ANIGAMES_LIST

    @staticmethod
    def osu():
        """
        ## Description
        --------------
        This function will return a list of Osu categories endpoints.

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        def osu():
            print(Estrapy.Help.osu()) # Keep it as function or it will return function type
        ```
        """

        OSU_LIST = ["osuprofile", "osubeatmap"]

        return OSU_LIST

    @staticmethod
    def trivia():
        """
        Description
        --------------
        This function will return a list of Trivia categories endpoints.

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        def trivia():
            print(Estrapy.Help.trivia()) # Keep it as function or it will return function type
        ```
        """

        TRIVIA_LIST = ["add", "remove", "answer", "run", "run_console"]

        return TRIVIA_LIST

    def all(self):
        """
        Description
        --------------
        This function will return a list of All categories endpoints (Sfw, Nsfw, Games, AniGames).

        ## Short Example
        ----------------------------

        ```
        import Estrapy

        def all():
            help = Estrapy.Help()
            print(help.all()) # Keep it as function or it will return function type
        ```

        """

        ALL_DICT = {
            "SFW": f", ".join(self.sfw()),
            "NSFW": f", ".join(self.nsfw()),
            "GAMES_LIST": f", ".join(self.games()),
            "ANIGAMES_LIST": f", ".join(self.anigames()),
            "TRIVIA_LIST": f", ".join(self.trivia()),
            "OSU_LIST": f", ".join(self.osu()),
        }

        return ALL_DICT
