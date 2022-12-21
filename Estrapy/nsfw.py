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
        """
        ## Description
        --------------
        This function will be returning an `Anime K1lling GIF` as url.
        If you want to generate more than one GIF, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def kill():
            one = await Estrapy.Nsfw.kill()
            five = await Estrapy.Nsfw.kill(generate=5)
            print(f"Generate One: {one.url} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
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
            output = await self.base.produce(total=generate, route=route, type="link")
            properties = PropertiesManager(urls=output)

        return properties

    async def yuri(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning an `Anime Yuri GIF/Image` as url.
        If you want to generate more than one GIF/Image, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def yuri():
            one = await Estrapy.Nsfw.yuri()
            five = await Estrapy.Nsfw.yuri(generate=5)
            print(f"Generate One: {one.url} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
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
            output = await self.base.produce(total=generate, route=route, type="link")
            properties = PropertiesManager(urls=output)

        return properties

    async def yaoi(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning an `Anime Yaoi GIF/Image` as url.
        If you want to generate more than one GIF/Image, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def yaoi():
            one = await Estrapy.Nsfw.yaoi()
            five = await Estrapy.Nsfw.yaoi(generate=5)
            print(f"Generate One: {one.url} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
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
            output = await self.base.produce(total=generate, route=route, type="link")
            properties = PropertiesManager(urls=output)

        return properties
