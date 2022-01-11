from .http import get_api

__all__ = ("Sfw",)


class Sfw:
    @staticmethod
    async def run():
        """
        Description
        --------------
        A Function That Will Return a SFW Run as GIFs

        How to use run function (Examples)
        ----------------------------
        ```
        Estrapy.Sfw.run() # Keep it as function or it will return function type
        ```
        """

        return get_api("sfw/run")["link"]

    @staticmethod
    async def hug():
        """
        Description
        --------------
        A Function That Will Return a SFW Hug as GIFs

        How to use hug function (Examples)
        ----------------------------
        ```
        Estrapy.Sfw.hug() # Keep it as function or it will return function type
        ```
        """

        return get_api("sfw/hug")["link"]

    @staticmethod
    async def smile():
        """
        Description
        --------------
        A Function That Will Return a SFW Smile as GIFs

        How to use smile function (Examples)
        ----------------------------
        ```
        Estrapy.Sfw.smile() # Keep it as function or it will return function type
        ```
        """

        return get_api("sfw/smile")["link"]

    @staticmethod
    async def headpat():
        """
        Description
        --------------
        A Function That Will Return a SFW Headpat as GIFs

        How to use headpat function (Examples)
        ----------------------------
        ```
        Estrapy.Sfw.headpat() # Keep it as function or it will return function type
        ```
        """

        return get_api("sfw/headpat")["link"]

    @staticmethod
    async def poke():
        """
        Description
        --------------
        A Function That Will Return a SFW Poke as GIFs

        How to use poke function (Examples)
        ----------------------------
        ```
        Estrapy.Sfw.poke() # Keep it as function or it will return function type
        """

        return get_api("sfw/poke")["link"]

    @staticmethod
    async def bite():
        """
        Description
        --------------
        A Function That Will Return a SFW Bite as GIFs

        How to use bite function (Examples)
        ----------------------------
        ```
        Estrapy.Sfw.bite() # Keep it as function or it will return function type
        ```
        """

        return get_api("sfw/bite")["link"]

    @staticmethod
    async def neko():
        """
        Description
        --------------
        A Function That Will Return a SFW Neko as GIFs/PNG

        How to use neko function (Examples)
        ----------------------------
        ```
        Estrapy.Sfw.neko() # Keep it as function or it will return function type
        ```
        """

        return get_api("sfw/neko")["link"]

    @staticmethod
    async def highfive():
        """
        Description
        --------------
        A Function That Will Return a SFW Highfive as GIFs

        How to use highfive function (Examples)
        ----------------------------
        ```
        Estrapy.Sfw.highfive() # Keep it as function or it will return function type
        ```
        """

        return get_api("sfw/highfive")["link"]

    @staticmethod
    async def slap():
        """
        Description
        --------------
        A Function That Will Return a SFW Slap as GIFs

        How to use slap function (Examples)
        ----------------------------
        ```
        Estrapy.Sfw.slap() # Keep it as function or it will return function type
        ```
        """

        return get_api("sfw/slap")["link"]
