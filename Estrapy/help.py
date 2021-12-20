__all__ = ("SFW_LIST", "NSFW_LIST", "Help")


SFW_LIST = ["hug", "run", "smile", "headpat", "neko", "bite", "highfive", "poke", "slap"]
NSFW_LIST = ["yaoi", "yuri", "kill"]
GAMES_LIST = ["truth", "dare"]

class Help:
    @staticmethod
    def sfw():
        return SFW_LIST

    @staticmethod
    def nsfw():
        return NSFW_LIST

    @staticmethod
    def games():
        return GAMES_LIST

    @staticmethod
    def all():
        return SFW_LIST, NSFW_LIST, GAMES_LIST
