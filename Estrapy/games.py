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
        """
        ## Description
        --------------
        This function will be returning a `Truth Challenge` as text.
        If you want to generate more than one Text, use `generate` parameter and it will return a list.

        ## Short Example
        ----------------------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def truth():
            one = await Estrapy.Games.truth()
            five = await Estrapy.Games.truth(generate=5)
            print(f"Generate One: {one.text} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - generate: int -- Generate how many requests to return
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
            output = await self.base.produce(total=generate, route=route, type="text")
            properties = PropertiesManager(urls=output)

        return properties

    async def dare(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning a `Dare Challenge` as text.
        If you want to generate more than one Text, use `generate` parameter and it will return a list.

        ## Short Example
        ----------------------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def dare():
            one = await Estrapy.Games.dare()
            five = await Estrapy.Games.dare(generate=5)
            print(f"Generate One: {one.text} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - client: any -- EstraClient with token_user and user_id to keep track of how many requests you already have.
            - generate: int -- Generate how many requests to return
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
            output = await self.base.produce(total=generate, route=route, type="text")
            properties = PropertiesManager(urls=output)

        return properties

    async def shipper(self, json: dict = None):
        """
        ## Description
        --------------
        This function will retrieve image from the API server and return it as `PIL.Image` object.
        Keep in mind that this function will not having an update for a while,
        so you can create new issues on our github: https://github.com/StawaDev/Estrapy-API/issues with using label `enhancement`.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        _json = {
            "players": {
                "player_1": {
                    "name": "player_1",
                    "image_url": "xxxx",
                },
                "player_2": {
                    "name": "player_2",
                    "image_url": "xxxx",
                },
                "background": {
                    "background_url": "xxxx",
                    "background_width": 1280,
                },
            }
        }

        async def shipper():
            x = await Estrapy.Games.shipper(json=_json)
            x.save("Shipper.png")
        ```

        ## Arguments:
            - players: dict -- Set the player information
            - background: dict -- Set the background
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
        """
        ## Description
        --------------
        This function will be returning a `Truth Challenge (Anime Topic)` as text.
        If you want to generate more than one Text, use `generate` parameter and it will return a list.

        ## Short Example
        ----------------------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def truth():
            one = await Estrapy.AniGames.truth()
            five = await Estrapy.AniGames.truth(generate=5)
            print(f"Generate One: {one.text} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - client: any -- EstraClient with token_user and user_id to keep track of how many requests you already have.
            - generate: int -- Generate how many requests to return
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
            output = await self.base.produce(total=generate, route=route, type="text")
            properties = PropertiesManager(urls=output)

        return properties

    async def dare(self, generate: Optional[int] = None) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning a `Dare Challenge (Anime Topic)` as text.
        If you want to generate more than one Text, use `generate` parameter and it will return a list.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def dare():
            one = await Estrapy.AniGames.dare()
            five = await Estrapy.AniGames.dare(generate=5)
            print(f"Generate One: {one.text} Generate 5 as List: {five}")
        ```

        ## Arguments:
            - client: any -- EstraClient with token_user and user_id to keep track of how many requests you already have.
            - generate: int -- Generate how many requests to return
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
            output = await self.base.produce(total=generate, route=route, type="text")
            properties = PropertiesManager(urls=output)

        return properties

    async def waifu(self) -> PropertiesManager:
        """
        ## Description
        --------------
        This function will be returning a `Waifu Image (Anime Topic)` as url.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        async def waifu():
            x = await Estrapy.AniGames.waifu()
            print(x.character_name, x.url)
        ```

        ## Arguments:
            - client: any -- EstraClient with token_user and user_id to keep track of how many requests you already have.
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
        """
        ## Description
        --------------
        This function will be returning a `Husbando Image (Anime Topic)` as url.

        ## Short Example
        --------------

        ```
        import Estrapy

        async def husbando():
            x = await Estrapy.AniGames.husbando()
            print(x.character_name, x.url)
        ```

        ## Arguments:
            - client: any -- EstraClient with token_user and user_id to keep track of how many requests you already have.
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
        """
        ## Description
        --------------
        This function will be returning a shipping percentage of player and waifu as text.

        ## Short Example
        --------------

        ```
        async def shipper_waifu():
            x = await Estrapy.AniGames.shipper_waifu(player="Stawa")
            print(x.player, x.character_name, x.percentage)
        ```

        ## Arguments:
            - player: str -- Generate how many requests to return
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
        """
        ## Description
        --------------
        This function will be returning a shipping percentage of player and husbando as text.

        ## Short Example
        --------------

        ```
        async def shipper_husbando():
            x = await Estrapy.AniGames.shipper_husbando(player="Stawa")
            print(x.player, x.character_name, x.percentage)
        ```

        ## Arguments:
            - player: str -- Generate how many requests to return
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
