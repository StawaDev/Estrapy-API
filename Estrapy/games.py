from .http import get_api

__all__ = ("Games", "AniGames",)


class Games:
    @staticmethod
    def truth():
        """
        Description
        --------------
        A Function That Will Return a Random Truth Challenge

        How to use truth function (Examples)
        ----------------------------

        ```
        Estrapy.Games.truth() # Keep it as function or it will return function type
        ```
        """
        return get_api("games/truth")["text"]

    @staticmethod
    def dare():
        """
        Description
        --------------
        A Function That Will Return a Random Dare Challenge As Text

        How to use dare function (Examples)
        ----------------------------
        ```
        Estrapy.Games.dare() # Keep it as function or it will return function type
        ```
        """

        return get_api("games/dare")["text"]


class AniGames:
    @staticmethod
    def truth():
        """
        Description
        --------------
        A Function That Will Return a Random Truth About Anime Challenge

        How to use truth [about anime] as function (Examples)
        ----------------------------

        ```
        Estrapy.AniGames.truth() # Keep it as function or it will return function type
        ```
        """

        return get_api("anigames/truth")["text"]

    @staticmethod
    def dare():
        """
        Description
        --------------
        A Function That Will Return a Random Dare Challenge As Text

        How to use dare [about anime] function (Examples)
        ----------------------------
        ```
        Estrapy.AniGames.dare() # Keep it as function or it will return function type
        ```
        """

        return get_api("anigames/dare")["text"]
    
    @staticmethod
    def waifu():
        """
        Description
        --------------
        A Function That Will Return a Random Waifu Picture As PNG

        How to use waifu [about anime] function (Examples)
        ----------------------------
        ```
        Estrapy.AniGames.waifu() # Keep it as function or it will return function type
        ```
        """
        
    @staticmethod
    def husbando():
        """
        Description
        --------------
        A Function That Will Return a Random Husbando Picture As PNG

        How to use husbando [about anime] function (Examples)
        ----------------------------
        ```
        Estrapy.AniGames.husbando() # Keep it as function or it will return function type
        ```
        """