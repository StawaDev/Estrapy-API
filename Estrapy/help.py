__all__ = ("SFW_LIST", "NSFW_LIST", "Help")


SFW_LIST = ["hug", "run", "smile", "headpat", "neko", "bite", "highfive", "poke"]
NSFW_LIST = ["yaoi", "yuri", "kill"]


class Help:
    @staticmethod
    def sfw():
        return SFW_LIST

    @staticmethod
    def nsfw():
        return NSFW_LIST

    @staticmethod
    def all():
        return SFW_LIST, NSFW_LIST
