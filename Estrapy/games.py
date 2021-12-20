from .http import get_api

__all__ = ("Games",)

class Games:
    @staticmethod
    def truth():
        """
        A Function That Will Return a Random Truth Challenge
        """
        return get_api("games/truth")["text"]

    @staticmethod
    def dare():
        """
        A Function That Will Return a Random Dare Challenge
        """

        return get_api("games/dare")["text"]
