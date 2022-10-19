from .http import post_api
from .property import OsuProfileProperties, OsuBeatmapProperties
from typing import Union, Optional


__all__ = ("OsuClient",)


class OsuClient:
    def __init__(
        self,
        client_id: Union[int, str] = None,
        client_secret: str = None,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

    async def profile(
        self,
        client: Optional[any] = None,
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
            "user": user_id if not user_id else username,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        if client:
            _json = {
                "token_user": client.token_user,
                "user_id": client.user_id,
            }
            output = post_api(route="osu/user", json=_json)

        url = post_api(route="osu/user", json=_json)
        output = OsuProfileProperties(url)

        return output

    async def beatmap(
        self,
        client: Optional[any] = None,
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
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        if client:
            _json = {
                "token_user": client.token_user,
                "user_id": client.user_id,
            }
            output = post_api(route="osu/beatmap", json=_json)

        url = post_api("osu/beatmap", json=_json)
        output = OsuBeatmapProperties(url)

        return output
