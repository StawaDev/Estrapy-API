from .http import get_api, post_api
from .base import Base
from .property import PropertiesManager
from typing import Optional

__all__ = ("Sfw",)


class Sfw:
    __slots__ = ("token_user", "user_id")

    def __init__(self, token_user: Optional[str] = None, user_id: Optional[int] = None):
        self.token_user = token_user
        self.user_id = user_id

    async def run(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning an `Anime Running GIF` as url.
        If you want to generate more than one GIF, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def run():
            one = await Estrapy.Sfw.run()
            five = await Estrapy.Sfw.run(generate=5)
            print(f"Generate One: {{one.url}} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
        """

        route = "sfw/run"
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

    async def hug(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning an `Anime Hugging GIF` as url.
        If you want to generate more than one GIF, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def hug():
            one = await Estrapy.Sfw.hug()
            five = await Estrapy.Sfw.hug(generate=5)
            print(f"Generate One: {one.url} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
        """

        route = "sfw/hug"
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

    async def smile(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning an `Anime Smiling GIF` as url.
        If you want to generate more than one GIF, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def smile():
            one = await Estrapy.Sfw.smile()
            five = await Estrapy.Sfw.smile(generate=5)
            print(f"Generate One: {one.url} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
        """

        route = "sfw/smile"
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

    async def headpat(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning an `Anime Headpat GIF` as url.
        If you want to generate more than one GIF, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def headpat():
            one = await Estrapy.Sfw.headpat()
            five = await Estrapy.Sfw.headpat(generate=5)
            print(f"Generate One: {one.url} Generate 5 as List: {five}")
        ```

         ## Arguments:
            - generate: int -- Generate how many requests to return
        """

        route = "sfw/headpat"
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

    async def poke(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning an `Anime Poke GIF` as url.
        If you want to generate more than one GIF, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def poke():
            one = await Estrapy.Sfw.poke()
            five = await Estrapy.Sfw.poke(generate=5)
            print(f"Generate One: {one.url} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
        """

        route = "sfw/poke"
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

    async def bite(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning an `Anime Bitting GIF` as url.
        If you want to generate more than one GIF, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def bite():
            one = await Estrapy.Sfw.bite()
            five = await Estrapy.Sfw.bite(generate=5)
            print(f"Generate One: {one.url} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
        """

        route = "sfw/bite"
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

    async def neko(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning an `Anime Neko Image` as url.
        If you want to generate more than one Image, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def neko():
            one = await Estrapy.Sfw.neko()
            five = await Estrapy.Sfw.neko(generate=5)
            print(f"Generate One: {one.url} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
        """

        route = "sfw/neko"
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

    async def highfive(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning an `Anime Highfive GIF` as url.
        If you want to generate more than one GIF, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def highfive():
            one = await Estrapy.Sfw.highfive()
            five = await Estrapy.Sfw.highfive(generate=5)
            print(f"Generate One: {one.url} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
        """

        route = "sfw/highfive"
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

    async def slap(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning an `Anime Slapping GIF` as url.
        If you want to generate more than one GIF, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def slap():
            one = await Estrapy.Sfw.slap()
            five = await Estrapy.Sfw.slap(generate=5)
            print(f"Generate One: {one.url} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
        """

        route = "sfw/slap"
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
