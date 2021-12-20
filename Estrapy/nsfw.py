from .http import get_api

__all__ = ("Nsfw",)


class Nsfw:
    @staticmethod
    def kill():
        """
        A Function That Will Return a NSFW Kill GIFs/PNG
        """
        return get_api("nsfw/kill")["link"]

    @staticmethod
    def yuri():
        """
        A Function That Will Return a NSFW Yuri GIFs/PNG
        """
        return get_api("nsfw/yuri")["link"]

    @staticmethod
    def yaoi():
        """
        A Function That Will Return a NSFW Yaoi GIFs/PNG
        """
        
        return get_api("nsfw/yaoi")["link"]
