from typing import Optional
from .http import get_api
from .base import Base

__all__ = ("Nsfw",)


class Nsfw:
    @staticmethod
    async def kill(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a NSFW Kill as GIFs/PNG

        How to use kill function (Examples)
        ----------------------------

        ```
        async def kill():
            print(await Estrapy.Nsfw.kill()) # Keep it as function or it will return function type
        ```

        :param generate
        :type int
        """

        url = "nsfw/kill"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]

    @staticmethod
    async def yuri(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a NSFW Yuri as GIFs/PNG

        How to use yuri function (Examples)
        ----------------------------
        ```
        async def yuri():
            print(await Estrapy.Nsfw.yuri()) # Keep it as function or it will return function type
        ```

        :param generate
        :type int
        """

        url = "nsfw/yuri"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]

    @staticmethod
    async def yaoi(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a NSFW Yaoi as GIFs/PNG

        How to use yaoi function (Examples)
        ----------------------------
        ```
        async def yaoi():
            print(await Estrapy.Nsfw.yaoi()) # Keep it as function or it will return function type
        ```

        :param generate
        :type int
        """

        url = "nsfw/yaoi"
        if generate:
            return Base.produce(total=generate, full_url=url, type="link")
        return get_api(url)["link"]
