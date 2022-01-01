from .http import get_api

__all__ = ("Data",)
TypeText = ["truth", "dare"]


class Data:
    @staticmethod
    def totalSfw(EndPoint):
        """
        Description
        --------------
        A Function That Will Return Total Image Sfw with Specific EndPoint

        How to use totalSfw function (Examples)
        ----------------------------

        ```
        Estrapy.Data.totalSfw() # Keep it as function or it will return function type
        ```
        """
        return get_api(f"sfw/{EndPoint}")["total_image"]

    @staticmethod
    def totalNsfw(EndPoint):
        """
        Description
        --------------
        A Function That Will Return Total Image Nsfw with Specific EndPoint

        How to use totalNsfw function (Examples)
        ----------------------------

        ```
        Estrapy.Data.totalNsfw() # Keep it as function or it will return function type
        ```
        """
        return get_api(f"nsfw/{EndPoint}")["total_image"]

    @staticmethod
    def totalGames(EndPoint):
        """
        Description
        --------------
        A Function That Will Return Total Text Games with Specific EndPoint

        How to use totalGames function (Examples)
        ----------------------------

        ```
        Estrapy.Data.totalGames() # Keep it as function or it will return function type
        ```
        """
        return get_api(f"games/{EndPoint}")["total_text"]

    @staticmethod
    def totalAniGames(EndPoint):
        """
        Description
        --------------
        A Function That Will Return Total Text/Image AniGames with Specific EndPoint

        How to use totalAniGames function (Examples)
        ----------------------------

        ```
        Estrapy.Data.totalAniGames() # Keep it as function or it will return function type
        ```
        """
        if EndPoint in TypeText:
            return get_api(f"anigames/{EndPoint}")["total_text"]
        else:
            return get_api(f"anigames/{EndPoint}")["total_image"]
