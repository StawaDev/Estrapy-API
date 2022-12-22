from .http import Requester
from .property import OsuProfileProperties, OsuBeatmapProperties
from typing import Optional


__all__ = ("OsuClient",)


class OsuClient:
    __slots__ = (
        "osu_client_id",
        "osu_client_secret",
        "client_id",
        "client_secret",
        "requester",
    )

    def __init__(
        self,
        osu_client_id: str = None,
        osu_client_secret: int = None,
        client_id: str = None,
        client_secret: int = None,
    ) -> None:
        self.osu_client_id = osu_client_id
        self.osu_client_secret = osu_client_secret
        self.client_id = client_id
        self.client_secret = client_secret
        self.requester = Requester()

    async def profile(
        self,
        user_id: Optional[int] = None,
        username: Optional[str] = None,
    ) -> OsuProfileProperties:
        """
        ## Description
        --------------
        This function is part of the Osu API and should be used only for fetching user's profile information.
        Also this function will be returning OsuProfileProperties object.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        async def profile():
            osu = Estrapy.OsuClient(
                client_id=xxxx, client_secret="xxxx"
            )
            x = await osu.profile(username="Stawa")
            print(x.avatar_url)
        ```

        ## Arguments:
            - user_id: Optional[int] -- Using `UserID` to retrieve user information, default is `None`.
            - username: Optional[str] -- Using `Username` to retrieve user information, default is `None`.
        """

        _json = {
            "user": username if not user_id else user_id,
            "osu_client_id": self.osu_client_id,
            "osu_client_secret": self.osu_client_secret,
        }

        if self.client_id and self.client_secret:
            _json.update(
                {
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                }
            )
            output = self.requester.post_api(route="osu/user", json=_json)

        url = self.requester.post_api(route="osu/user", json=_json)
        output = OsuProfileProperties(original_response=url)

        return output

    async def beatmap(
        self,
        beatmap_id: int = None,
    ) -> OsuBeatmapProperties:
        """
        ## Description
        --------------
        This function is part of the Osu API and should be used only for fetching beatmaps information.
        Also this function will be returning OsuBeatmapProperties object.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        async def beatmap():
            osu = Estrapy.OsuClient(
                client_id=xxxx, client_secret="xxxx"
            )
            x = await osu.beatmap(beatmap_id=123)
            print(x.beatmapset.artist)
        ```

        ## Arguments:
            - beatmap_id: int -- Using `BeatmapID` to retrieve user information, default is `None`.
        """

        _json = {
            "id": beatmap_id,
            "osu_client_id": self.osu_client_id,
            "osu_client_secret": self.osu_client_secret,
        }

        if self.client_id and self.client_secret:
            _json.update(
                {
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                }
            )
            output = self.requester.post_api(route="osu/user", json=_json)

        url = self.requester.post_api("osu/beatmap", json=_json)
        output = OsuBeatmapProperties(original_response=url)

        return output
