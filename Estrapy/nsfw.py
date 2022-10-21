from typing import Optional
from .http import get_api, post_api
from .base import Base
from .property import PropertiesManager

__all__ = ("Nsfw",)


class Nsfw:
    __slots__ = ("token_user", "user_id")

    def __init__(self, token_user: Optional[str] = None, user_id: Optional[int] = None):
        self.token_user = token_user
        self.user_id = user_id

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
        output = get_api(route=route)

        if self.token_user and self.user_id:
            _json = {
                "token_user": self.token_user,
                "user_id": self.user_id,
            }
            output = post_api(route=route, json=_json)

        properties = PropertiesManager(
            url=output.get("link"),
            type=output.get("type"),
            total=output.get("total_image"),
            with_account=output.get("with_account"),
        )

        if generate:
            return await Base.produce(total=generate, route=route, type="link")

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
        output = get_api(route=route)

        if self.token_user and self.user_id:
            _json = {
                "token_user": self.token_user,
                "user_id": self.user_id,
            }
            output = post_api(route=route, json=_json)

        properties = PropertiesManager(
            url=output.get("link"),
            type=output.get("type"),
            total=output.get("total_image"),
            with_account=output.get("with_account"),
        )

        if generate:
            return await Base.produce(total=generate, route=route, type="link")

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
        output = get_api(route=route)

        if self.token_user and self.user_id:
            _json = {
                "token_user": self.token_user,
                "user_id": self.user_id,
            }
            output = post_api(route=route, json=_json)

        properties = PropertiesManager(
            url=output.get("link"),
            type=output.get("type"),
            total=output.get("total_image"),
            with_account=output.get("with_account"),
        )

        if generate:
            return await Base.produce(total=generate, route=route, type="link")

        return properties
