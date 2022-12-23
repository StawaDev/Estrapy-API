from .http import Requester
from .base import Base
from .property import PropertiesManager
from typing import Optional
from io import BytesIO
from PIL import Image

__all__ = (
    "Games",
    "AniGames",
)


class Games:
    __slots__ = ("client_id", "client_secret", "requester", "base")

    def __init__(
        self, client_id: Optional[str] = None, client_secret: Optional[str] = None
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.requester = Requester()
        self.base = Base()

    async def truth(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will fetch the `Truth Challenge` from the API.

        Parameters
        -----------
        generate: Optional[int]
            Generate how many requests to return

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response; when users use `generate`, only the `url/text` and `with_account` properties will be available to use.
        """

        route = "games/truth"
        output = self.requester.get_api(route=route)

        if self.client_id and self.client_secret:
            _json = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            output = self.requester.post_api(route=route, json=_json)

        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
            with_account=output.get("with_account"),
            original_response=output,
        )

        if generate:
            output, with_account = await self.base.produce(
                total=generate, route=route, type="text"
            )
            properties = PropertiesManager(text=output, with_account=with_account)

        return properties

    async def dare(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will fetch the `Dare Challenge` from the API.

        Parameters
        -----------
        generate: Optional[int]
            Generate how many requests to return

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response; when users use `generate`, only the `url/text` and `with_account` properties will be available to use.
        """

        route = "games/dare"
        output = self.requester.get_api(route=route)

        if self.client_id and self.client_secret:
            _json = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            output = self.requester.post_api(route=route, json=_json)

        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
            with_account=output.get("with_account"),
            original_response=output,
        )

        if generate:
            output, with_account = await self.base.produce(
                total=generate, route=route, type="text"
            )
            properties = PropertiesManager(text=output, with_account=with_account)

        return properties

    async def shipper(self, json: dict = None):
        """This function will retrieve image from the API server and return it as `PIL.Image` object.
        Keep in mind that this function will not having an update for a while,
        so you can create new issues on our github: https://github.com/StawaDev/Estrapy-API/issues with using label `enhancement`.

        Parameters
        -----------
        players: dict
            Set the player information
        background: dict
            Set the background
        """

        route = "games/shipper"
        req = self.requester.post_response(route=route, json=json)

        if self.client_id and self.client_secret:
            _json = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            self.requester.post_api(route=route, json=_json)

        return Image.open(BytesIO(req.content))


class AniGames:
    __slots__ = ("client_id", "client_secret", "requester", "base")

    def __init__(
        self, client_id: Optional[str] = None, client_secret: Optional[int] = None
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.requester = Requester()
        self.base = Base()

    async def truth(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will fetch the `Truth Challenge` theme anime from the API.

        Parameters
        -----------
        generate: Optional[int]
            Generate how many requests to return

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response; when users use `generate`, only the `url/text` and `with_account` properties will be available to use.
        """

        route = "anigames/truth"
        output = self.requester.get_api(route=route)

        if self.client_id and self.client_secret:
            _json = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            output = self.requester.post_api(route=route, json=_json)

        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
            with_account=output.get("with_account"),
            original_response=output,
        )

        if generate:
            output, with_account = await self.base.produce(
                total=generate, route=route, type="text"
            )
            properties = PropertiesManager(text=output, with_account=with_account)

        return properties

    async def dare(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will fetch the `Dare Challenge` theme anime from the API.

        Parameters
        -----------
        generate: Optional[int]
            Generate how many requests to return

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response; when users use `generate`, only the `url/text` and `with_account` properties will be available to use.
        """

        route = "anigames/dare"
        output = self.requester.get_api(route=route)

        if self.client_id and self.client_secret:
            _json = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            output = self.requester.post_api(route=route, json=_json)

        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
            with_account=output.get("with_account"),
            original_response=output,
        )

        if generate:
            output, with_account = await self.base.produce(
                total=generate, route=route, type="text"
            )
            properties = PropertiesManager(text=output, with_account=with_account)

        return properties

    async def waifu(self) -> PropertiesManager:
        """This function will fetch Waifu Picture from the API.

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response.
        """

        route = "anigames/waifu"
        output = self.requester.get_api(route=route)

        if self.client_id and self.client_secret:
            _json = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            output = self.requester.post_api(route=route, json=_json)

        properties = PropertiesManager(
            url=output.get("link"),
            type=output.get("type"),
            character_name=output.get("character_name"),
            total=output.get("total_image"),
            with_account=output.get("with_account"),
            original_response=output,
        )

        return properties

    async def husbando(self) -> PropertiesManager:
        """This function will fetch the Husbando Picture from the API.

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response.
        """

        route = "anigames/husbando"
        output = self.requester.get_api(route=route)

        if self.client_id and self.client_secret:
            _json = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            output = self.requester.post_api(route=route, json=_json)

        properties = PropertiesManager(
            url=output.get("link"),
            type=output.get("type"),
            character_name=output.get("character_name"),
            total=output.get("total_image"),
            with_account=output.get("with_account"),
            original_response=output,
        )

        return properties

    async def shipper_waifu(self, player: str = None) -> PropertiesManager:
        """This function will fetch `shipper_waifu` from the API.

        Parameters
        -----------
        player: str
            Player's name to ship with.

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response.
        """

        route = f"anigames/shipper/waifu/?player={player}"
        output = self.requester.get_api(route=route)

        if self.client_id and self.client_secret:
            _json = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            output = self.requester.post_api(route=route, json=_json)

        properties = PropertiesManager(
            player=output.get("player"),
            character_name=output.get("character_name"),
            percentage=output.get("percentage"),
            with_account=output.get("with_account"),
            original_response=output,
        )

        return properties

    async def shipper_husbando(self, player: str = None) -> PropertiesManager:
        """This function will fetch `shipper_husbando` from the API.

        Parameters
        -----------
        player: str
            Player's name to ship with.

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response.
        """

        route = f"anigames/shipper/husbando/?player={player}"
        output = self.requester.get_api(route=route)

        if self.client_id and self.client_secret:
            _json = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            output = self.requester.post_api(route=route, json=_json)

        properties = PropertiesManager(
            player=output.get("player"),
            character_name=output.get("character_name"),
            percentage=output.get("percentage"),
            with_account=output.get("with_account"),
            original_response=output,
        )

        return properties
