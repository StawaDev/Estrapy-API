from typing import Optional
from .http import get_api
from .base import Base

__all__ = ("Sfw",)


class Sfw:
    @staticmethod
    async def run(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a SFW Run as GIFs

        How to use run function (Examples)
        ----------------------------
        ```
        async def run():
            print(await Estrapy.Sfw.run()) # Keep it as function or it will return function type
        ```

        :param generate
        :type int
        """

        url = "sfw/run"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]

    @staticmethod
    async def hug(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a SFW Hug as GIFs

        How to use hug function (Examples)
        ----------------------------
        ```
        async def hug():
            print(await Estrapy.Sfw.hug()) # Keep it as function or it will return function type
        ```

        :param generate
        :type int
        """

        url = "sfw/hug"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]

    @staticmethod
    async def smile(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a SFW Smile as GIFs

        How to use smile function (Examples)
        ----------------------------
        ```
        async def smile():
            print(await Estrapy.Sfw.smile()) # Keep it as function or it will return function type
        ```

        :param generate
        :type int
        """

        url = "sfw/smile"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]

    @staticmethod
    async def headpat(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a SFW Headpat as GIFs

        How to use headpat function (Examples)
        ----------------------------
        ```
        async def headpat():
            print(await Estrapy.Sfw.headpat()) # Keep it as function or it will return function type
        ```

        :param generate
        :type int
        """

        url = "sfw/headpat"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]

    @staticmethod
    async def poke(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a SFW Poke as GIFs

        How to use poke function (Examples)
        ----------------------------
        ```
        async def poke():
            print(await Estrapy.Sfw.poke()) # Keep it as function or it will return function type
        ```

        :param generate
        :type int
        """

        url = "sfw/poke"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]

    @staticmethod
    async def bite(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a SFW Bite as GIFs

        How to use bite function (Examples)
        ----------------------------
        ```
        async def bite():
            print(await Estrapy.Sfw.bite()) # Keep it as function or it will return function type
        ```

        :param generate
        :type int
        """

        url = "sfw/bite"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]

    @staticmethod
    async def neko(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a SFW Neko as GIFs/PNG

        How to use neko function (Examples)
        ----------------------------
        ```
        async def neko():
            print(await Estrapy.Sfw.neko()) # Keep it as function or it will return function type
        ```

        :param generate
        :type int
        """

        url = "sfw/neko"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]

    @staticmethod
    async def highfive(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a SFW Highfive as GIFs

        How to use highfive function (Examples)
        ----------------------------
        ```
        async def highfive():
            print(await Estrapy.Sfw.highfive()) # Keep it as function or it will return function type
        ```
        """

        url = "sfw/highfive"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]

    @staticmethod
    async def slap(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a SFW Slap as GIFs

        How to use slap function (Examples)
        ----------------------------
        ```
        async def slap():
            print(await Estrapy.Sfw.slap()) # Keep it as function or it will return function type
        ```
        """

        url = "sfw/slap"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]
