from .http import get_api

__all__ = ("Sfw",)


class Sfw:
    @staticmethod
    def run():
        """
        A Function That Will Return a SFW Run GIFs
        """

        return get_api("sfw/run")["link"]

    @staticmethod
    def hug():
        """
        A Function That Will Return a SFW Hug GIFs
        """

        return get_api("sfw/hug")["link"]

    @staticmethod
    def smile():
        """
        A Function That Will Return a SFW Smile GIFs
        """

        return get_api("sfw/smile")["link"]

    @staticmethod
    def headpat():
        """A Function That Will Return a SFW Headpat GIFs"""

        return get_api("sfw/headpat")["link"]

    @staticmethod
    def poke():
        """
        A Function That Will Return a SFW Poke GIFs
        """

        return get_api("sfw/poke")["link"]

    @staticmethod
    def bite():
        """
        A Function That Will Return a SFW Bite GIFs
        """

        return get_api("sfw/bite")["link"]

    @staticmethod
    def neko():
        """
        A Function That Will Return a SFW Neko GIFs/PNG
        """

        return get_api("sfw/neko")["link"]

    @staticmethod
    def highfive():
        """
        A Function That Will Return a SFW Highfive GIFs
        """
        
        return get_api("sfw/highfive")["link"]
    
    @staticmethod
    def slap():
        """
        A Function That Will Return a SFW Slap GIFs
        """
        
        return get_api("sfw/slap")["link"]