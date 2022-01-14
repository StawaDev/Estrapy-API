from typing import Union, Optional
from .http import get_api
from .base import Base

__all__ = ("Games", "AniGames", "OsuClients")


class Games:
    @staticmethod
    async def truth(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a Random Truth Challenge

        How to use truth function (Examples)
        ----------------------------

        ```
        async def truth():
            print(await Estrapy.Games.truth()) # Keep it as function or it will return function type
        ```

        :param generate
        :type formatter: Optional[int]
        """

        url = "games/truth"
        if generate:
            return await Base.produce(total=generate, full_url=url, type="text")

        return get_api(url)["text"]

    @staticmethod
    async def dare(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a Random Dare Challenge As Text

        How to use dare function (Examples)
        ----------------------------
        ```
        async def truth():
            print(await Estrapy.Games.truth()) # Keep it as function or it will return function type
        ```

        :param generate
        :type formatter: Optional[int]
        """

        url = "games/dare"
        if generate:
            return await Base.produce(total=generate, full_url=url, type="text")
        return get_api(url)["text"]


class AniGames:
    @staticmethod
    async def truth(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a Random Truth About Anime Challenge

        How to use truth [about anime] as function (Examples)
        ----------------------------

        ```
        async def truth():
            print(await Estrapy.AniGames.truth()) # Keep it as function or it will return function type
        ```

        :param generate
        :type formatter: Optional[int]
        """

        url = "anigames/truth"
        if generate:
            return await Base.produce(total=generate, full_url=url, type="text")
        return get_api(url)["text"]

    @staticmethod
    async def dare(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a Random Dare Challenge As Text

        How to use dare [about anime] function (Examples)
        ----------------------------
        ```
        async def dare():
            print(await Estrapy.AniGames.dare()) # Keep it as function or it will return function type
        ```

        :param generate
        :type formatter: Optional[int]
        """

        url = "anigames/dare"
        if generate:
            return await Base.produce(total=generate, full_url=url, type="text")
        return get_api(url)["text"]

    @staticmethod
    async def waifu(formatter: bool = False):
        """
        Description
        --------------
        A Function That Will Return a Random Waifu Picture As PNG

        How to use waifu [about anime] function (Examples)
        ----------------------------
        ```
        async def waifu():
            print(await Estrapy.AniGames.waifu()) # Keep it as function or it will return function type
        ```

        :param formatter
        :type formatter: bool, default `False`
        """
        url = get_api("anigames/waifu")
        if formatter:
            return await Base.JSONFormatter(url)
        return url

    @staticmethod
    async def husbando(formatter: bool = False):
        """
        Description
        --------------
        A Function That Will Return a Random Husbando Picture As PNG

        How to use husbando [about anime] function (Examples)
        ----------------------------
        ```
        async def husbando():
            print(await Estrapy.AniGames.husbando()) # Keep it as function or it will return function type
        ```

        :param formatter
        :type formatter: bool, default `False`
        """

        url = get_api("anigames/husbando")
        if formatter:
            return await Base.JSONFormatter(url)
        return url

    @staticmethod
    async def shipper_waifu(player: str, formatter: bool = False):
        """
        Shipper_Waifu
        --------------
        Return Shipper Waifu JSON Data from EstraAPI

        Examples
        --------------
        ```
        async def shipper_husbando():
            print(await Estrapy.AniGames.shipper_husbando(player="Stawa"))
        ```

        :param player
        :type player: str
        :param formatter
        :type formatter: bool, default `False`
        """

        url = get_api(f"anigames/shipper/waifu/?player={player}")
        if formatter:
            return await Base.JSONFormatter(url)
        return url

    @staticmethod
    async def shipper_husbando(player: str, formatter: bool = False):
        """
        Shipper_Husbando
        --------------
        Return Shipper Husbando JSON Data from EstraAPI

        Examples
        --------------
        ```
        async def shipper_husbando():
            print(await Estrapy.AniGames.shipper_husbando(player="Stawa"))
        ```

        :param player
        :type player: str
        :param formatter
        :type formatter: bool, default `False`
        """

        url = get_api(f"anigames/shipper/husbando/?player={player}")
        if formatter:
            return await Base.JSONFormatter(url)
        return url


class OsuClients:
    def __init__(self, client_id: Union[int, str], client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

    def client_data(self):
        """
        Client_Data
        --------------

        Keep as function of OsuClients, you can print this function to return your client_id and client_secret
        """

        global clientid, clientsecret
        clientid = self.client_id
        clientsecret = self.client_secret
        return f"Estrapy OsuClients Data: \nClient_ID: {clientid} \nClient_Secret: {clientsecret}"

    @staticmethod
    async def osuprofile(
        username: Union[int, str],
        formatter: bool = False,
    ):
        """
        Osuprofile
        --------------
        Return Osuprofile JSON Data

        Examples
        --------------
        ```
        async def osuprofile():
            print(await Estrapy.OsuClients.osuprofile(username="Stawa"))
        ```

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
            f"osu/?user={username}&client_id={clientid}&client_secret={clientsecret}"
        )
        if formatter:
            return await Base.JSONFormatter(url)
        return url

    @staticmethod
    async def osubeatmap(
        beatmap_id: int,
        formatter: bool = False,
    ):
        """
        Osubeatmap
        --------------
        Return Osubeatmap JSON Data

        Examples
        --------------
        ```
        async def osubeatmap():
            print(await Estrapy.OsuClients.osubeatmap(beatmap_id="2405223"))
        ```

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
            f"osubeatmap/?id={beatmap_id}&client_id={clientid}&client_secret={clientsecret}"
        )
        if formatter:
            return await Base.JSONFormatter(url)
        return url
