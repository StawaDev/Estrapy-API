__all__ = ("Help",)


class Help:
    """A simple help class with functions that can return all available category endpoints"""

    @staticmethod
    def sfw() -> list[str]:
        """This function will return a list of `Sfw` category endpoints.

        Returns
        --------
        list[str]
            Return a list filled with SFW endpoints.
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
    def nsfw() -> list[str]:
        """This function will return a list of `Nsfw` category endpoints.

        Returns
        --------
        list[str]
            Return a list filled with NSFW endpoints.
        """

        NSFW_LIST = ["yaoi", "yuri", "kill"]

        return NSFW_LIST

    @staticmethod
    def games() -> list[str]:
        """This function will return a list of `Games` category endpoints.

        Returns
        --------
        list[str]
            Return a list filled with Games endpoints.
        """

        GAMES_LIST = ["truth", "dare", "shipper"]

        return GAMES_LIST

    @staticmethod
    def anigames() -> list[str]:
        """This function will return a list of `AniGames` category endpoints.

        Returns
        --------
        list[str]
            Return a list filled with AniGames endpoints.
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
    def osu() -> list[str]:
        """This function will return a list of `Osu` category endpoints.

        Returns
        --------
        list[str]
            Return a list filled with Osu endpoints.
        """

        OSU_LIST = ["osuprofile", "osubeatmap"]

        return OSU_LIST

    @staticmethod
    def trivia() -> list[str]:
        """This function will return a list of `Trivia` functions.

        Returns
        --------
        list[str]
            Return a list filled with Trivia functions.
        """

        TRIVIA_LIST = ["add", "remove", "answer", "run", "run_console"]

        return TRIVIA_LIST

    def all(self) -> dict:
        """This function will return a dict with all category endpoints.

        Returns
        --------
        dict
            Return a dict filled with all category endpoints.
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
