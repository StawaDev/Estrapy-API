from typing import Optional
from .http import Requester
from .base import Base
from .property import PropertiesManager

__all__ = ("Nsfw",)


class Nsfw:
    __slots__ = ("client_id", "client_secret", "requester", "base")

    def __init__(
        self, client_id: Optional[str] = None, client_secret: Optional[int] = None
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.requester = Requester()
        self.base = Base()

    async def kill(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime K1lling GIF` as url.
        If you want to generate more than one GIF, use `generate` parameter and it will return a list.

        Parameters
        -----------
        generate: Optional[int]
            Generate how many requests to return

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response; when users use `generate`, only the `url/text` and `with_account` properties will be available to use.
        """

        route = "nsfw/kill"
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
            total=output.get("total_image"),
            with_account=output.get("with_account"),
            original_response=output,
        )

        if generate:
            output, with_account = await self.base.produce(
                total=generate, route=route, type="link"
            )
            properties = PropertiesManager(url=output, with_account=with_account)

        return properties

    async def yuri(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime Yuri GIF/Image` as url.
        If you want to generate more than one GIF/Image, use `generate` parameter and it will return a list.

        Parameters
        -----------
        generate: Optional[int]
            Generate how many requests to return

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response; when users use `generate`, only the `url/text` and `with_account` properties will be available to use.
        """

        route = "nsfw/yuri"
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
            total=output.get("total_image"),
            with_account=output.get("with_account"),
            original_response=output,
        )

        if generate:
            output, with_account = await self.base.produce(
                total=generate, route=route, type="link"
            )
            properties = PropertiesManager(url=output, with_account=with_account)

        return properties

    async def yaoi(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime Yaoi GIF/Image` as url.
        If you want to generate more than one GIF/Image, use `generate` parameter and it will return a list.

        Parameters
        -----------
        generate: Optional[int]
            Generate how many requests to return

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response; when users use `generate`, only the `url/text` and `with_account` properties will be available to use.
        """

        route = "nsfw/yaoi"
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
            total=output.get("total_image"),
            with_account=output.get("with_account"),
            original_response=output,
        )

        if generate:
            output, with_account = await self.base.produce(
                total=generate, route=route, type="link"
            )
            properties = PropertiesManager(url=output, with_account=with_account)

        return properties
