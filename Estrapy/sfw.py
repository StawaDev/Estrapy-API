from .http import get_api

__all__ = ("Sfw",)


class Sfw:
    @staticmethod
    def run():
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
    def hug():
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
    def smile():
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
    def headpat():
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
    def poke():
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
    def bite():
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
    def neko():
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
    def highfive():
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
    def slap():
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