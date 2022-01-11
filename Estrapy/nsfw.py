from .http import get_api

__all__ = ("Nsfw",)


class Nsfw:
    @staticmethod
    async def kill():
        """
        Description
        --------------
        A Function That Will Return a NSFW Kill as GIFs/PNG

        How to use kill function (Examples)
        ----------------------------

        ```
        Estrapy.Nsfw.kill() # Keep it as function or it will return function type
        ```
        """
        return get_api("nsfw/kill")["link"]

    @staticmethod
    async def yuri():
        """
        Description
        --------------
        A Function That Will Return a NSFW Yuri as GIFs/PNG

        How to use yuri function (Examples)
        ----------------------------
        Estrapy.Nsfw.yuri() # Keep it as function or it will return function type
        ```
        """
        return get_api("nsfw/yuri")["link"]

    @staticmethod
    async def yaoi():
        """
        Description
        --------------
        A Function That Will Return a NSFW Yaoi as GIFs/PNG

        How to use yaoi function (Examples)
        ----------------------------
        ```
        Estrapy.Nsfw.yaoi() # Keep it as function or it will return function type
        ```
        """

        return get_api("nsfw/yaoi")["link"]
