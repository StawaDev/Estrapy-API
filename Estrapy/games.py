from typing import Union
from .http import get_api
from .formatter import JSONFormatter

__all__ = ("Games", "AniGames", "OsuClients")


class Games:
    @staticmethod
    async def truth():
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
    async def dare():
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
    async def truth():
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
    async def dare():
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
    async def waifu():
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
        global waifu
        waifu = get_api("anigames/waifu")
        return waifu["link"]

    @staticmethod
    async def husbando():
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
        global husbando
        husbando = get_api("anigames/husbando")
        return husbando["link"]

    @staticmethod
    async def waifu_name():
        """
        Description
        --------------
        A Function That Will Return a Name Character of the Waifu Picture As Text

        How to use waifu_name [about anime] function (Examples)
        ----------------------------
        ```
        Estrapy.AniGames.waifu() # Keep it as function or it will return function type
        ```
        """
        character_name = waifu
        return character_name["character_name"]

    @staticmethod
    async def husbando_name():
        """
        Description
        --------------
        A Function That Will Return a Name Character of the Waifu Picture As Text

        How to use waifu_name [about anime] function (Examples)
        ----------------------------
        ```
        Estrapy.AniGames.waifu() # Keep it as function or it will return function type
        ```
        """
        character_name = husbando
        return character_name["character_name"]

    @staticmethod
    async def shipper_waifu(player: str, formatter: bool = False):
        """
        Shipper_Waifu
        --------------
        Return Shipper Waifu JSON Data from EstraAPI

        :param player
        :type player: str
        :param formatter
        :type formatter: bool, default `False`
        """
        if formatter:
            data = JSONFormatter(get_api(f"anigames/shipper/waifu/?player={player}"))
        else:
            data = get_api(f"anigames/shipper/waifu/?player={player}")
        return data

    @staticmethod
    async def shipper_husbando(player: str, formatter: bool = False):
        """
        Shipper_Husbando
        --------------
        Return Shipper Husbando JSON Data from EstraAPI

        :param player
        :type player: str
        :param formatter
        :type formatter: bool, default `False`
        """
        url = get_api(f"anigames/shipper/husbando/?player={player}")
        if formatter:
            data = JSONFormatter(url)
        else:
            data = url
        return data


class OsuClients:
    @staticmethod
    async def osuprofile(
        username: Union[int, str],
        client_id: Union[int, str],
        client_secret: str,
        formatter: bool = False,
    ):
        """
        Osuprofile
        --------------
        Return Osuprofile JSON Data

        :param username
        :type username: int or str
        :param client_id
        :type client_id: int
        :param client_secret
        :type client_secret: str
        :param formatter: It will formatting JSON Data with EstraFormatter
        :type formatter: bool, default `False`
        """
        url = get_api(
            f"osu/?user={username}&client_id={client_id}&client_secret={client_secret}"
        )
        if formatter:
            data = JSONFormatter(url)
        else:
            data = url
        return data

    @staticmethod
    async def osubeatmap(
        beatmap_id: int,
        client_id: Union[int, str],
        client_secret: str,
        formatter: bool = False,
    ):
        """
        Osubeatmap
        --------------
        Return Osubeatmap JSON Data

        :param beatmap_id
        :type beatmap_id: int or str
        :param client_id
        :type client_id: int
        :param client_secret
        :type client_secret: str
        :param formatter: It will formatting JSON Data with EstraFormatter
        :type formatter: bool, default `False`
        """
        url = get_api(
            f"osubeatmap/?id={beatmap_id}&client_id={client_id}&client_secret={client_secret}"
        )
        if formatter:
            data = JSONFormatter(url)
        else:
            data = url
        return data
