from .http import get_api

__all__ = ("Sfw",)


class Sfw:
    @staticmethod
    def run():
        """
        A Function That Will Return a SFW Run GIF
        """

        return get_api("sfw/run")["link"]

    @staticmethod
    def hug():
        """
        A Function That Will Return a SFW Hug GIF
        """

        return get_api("sfw/hug")["link"]

    @staticmethod
    def smile():
        """
        A Function That Will Return a SFW Smile GIF
        """

        return get_api("sfw/smile")["link"]

    @staticmethod
    def headpat():
        """A Function That Will Return a SFW Headpat GIF"""

        return get_api("sfw/headpat")["link"]

    @staticmethod
    def poke():
        """
        A Function That Will Return a SFW Poke GIF
        """

        return get_api("sfw/poke")["link"]

    @staticmethod
    def bite():
        """
        A Function That Will Return a SFW Bite GIF
        """

        return get_api("sfw/bite")["link"]

    @staticmethod
    def neko():
        """
        A Function That Will Return a SFW Neko GIF
        """

        return get_api("sfw/neko")["link"]

    @staticmethod
    def highfive():
        """
        A Function That Will Return a SFW Highfive GIF
        """
        
        return get_api("sfw/highfive")["link"]
    
    @staticmethod
    def slap():
        """
        A Function That Will Return a SFW Slap GIF
        """
        
        return get_api("sfw/slap")["link"]