from .http import Requester
from .property import AccountProperties, AccountStatistics
import json

__all__ = ("AccountManager",)


class AccountManager:
    def __init__(self, client_id: str, client_secret: str):
        self.requester = Requester(custom_url="https://estra-db.vercel.app/")
        self.client_id = client_id
        self.client_secret = client_secret

    def properties(self) -> AccountProperties:
        req = self.requester.post_api(
            json={"client_id": self.client_id, "client_secret": self.client_secret}
        )

        return AccountProperties(
            username=req.get("username"),
            uid=req.get("uid"),
            client_id=req.get("client_id"),
            client_secret=req.get("client_secret"),
        )

    def statistics(self) -> AccountStatistics:
        req = self.requester.post_api(
            route="statistics",
            json={"client_id": self.client_id, "client_secret": self.client_secret},
        )

        return AccountStatistics(
            sfw=json.loads(json.dumps(req.get("sfw"))),
            nsfw=json.loads(json.dumps(req.get("nsfw"))),
            games=json.loads(json.dumps(req.get("games"))),
            anigames=json.loads(json.dumps(req.get("anigames"))),
            osu=json.loads(json.dumps(req.get("osu"))),
            total_requests_user=req.get("total_requests_user"),
        )
