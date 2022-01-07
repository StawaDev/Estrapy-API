from .http import get_api

__all__ = ("OsuClients")

class OsuClients:
    @staticmethod
    def osuprofile(username, data, client_id, client_secret):
        return get_api(f"osu/?user={username}&client_id={client_id}&client_secret={client_secret}")[f"{data}"]