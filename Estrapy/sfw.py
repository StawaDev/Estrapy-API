from .http import Requester
from .base import Base
from .property import PropertiesManager
from typing import Optional

__all__ = ("Sfw",)


class Sfw:
    __slots__ = ("client_id", "client_secret", "requester", "base")

    def __init__(
        self, client_id: Optional[str] = None, client_secret: Optional[int] = None
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.requester = Requester()
        self.base = Base()

    async def run(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime Running GIF` as url.
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

        route = "sfw/run"
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

    async def hug(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime Hugging GIF` as url.
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

        route = "sfw/hug"
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

    async def smile(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime Smiling GIF` as url.
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

        route = "sfw/smile"
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

    async def headpat(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime Headpat GIF` as url.
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

        route = "sfw/headpat"
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

    async def poke(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime Poke GIF` as url.
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

        route = "sfw/poke"
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

    async def bite(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime Bitting GIF` as url.
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

        route = "sfw/bite"
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

    async def neko(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime Neko Image` as url.
        If you want to generate more than one Image, use `generate` parameter and it will return a list.

        Parameters
        -----------
        generate: Optional[int]
            Generate how many requests to return

        Returns
        --------
        :class:`~Estrapy.property.PropertiesManager`
            Return a class object containing the complete API response; when users use `generate`, only the `url/text` and `with_account` properties will be available to use.
        """

        route = "sfw/neko"
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

    async def highfive(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime Highfive GIF` as url.
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

        route = "sfw/highfive"
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

    async def slap(self, generate: Optional[int] = None) -> PropertiesManager:
        """This function will be returning an `Anime Slapping GIF` as url.
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

        route = "sfw/slap"
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
