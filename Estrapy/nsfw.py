from .http import get_api

__all__ = ("Nsfw",)


class Nsfw:
    @staticmethod
    def kill():
        return get_api("nsfw/kill")["link"]

    @staticmethod
    def yuri():
        return get_api("nsfw/yuri")["link"]

    @staticmethod
    def yaoi():
        return get_api("nsfw/yaoi")["link"]
