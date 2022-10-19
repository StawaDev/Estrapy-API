from .http import get_api, post_api
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
    @staticmethod
    async def truth(
        client: Optional[any] = None, generate: Optional[int] = None
    ) -> PropertiesManager:
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
            - client: any -- EstraClient with token_user and user_id to keep track of how many requests you already have.
            - generate: int -- Generate how many requests to return
        """

        route = "games/truth"
        output = get_api(route=route)

        if client:
            _json = {
                "token_user": client.token_user,
                "user_id": client.user_id,
            }
            output = post_api(route=route, json=_json)

        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
            with_account=output.get("with_account"),
        )

        if generate:
            return await Base.produce(total=generate, route=route, type="text")

        return properties

    @staticmethod
    async def dare(
        client: Optional[any] = None, generate: Optional[int] = None
    ) -> PropertiesManager:
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
        output = get_api(route=route)

        if client:
            _json = {
                "token_user": client.token_user,
                "user_id": client.user_id,
            }
            output = post_api(route=route, json=_json)

        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
            with_account=output.get("with_account"),
        )

        if generate:
            return await Base.produce(total=generate, route=route, type="text")

        return properties

    @staticmethod
    async def shipper(players: dict, background: dict = None):
        """
        ## Description
        --------------
        This function will retrieve image from the API server and return it as `PIL.Image` object.
        Keep in mind that this function will not having an update for a while,
        so you can create new issues on our github: https://github.com/StawaDev/Estrapy-API/issues with using label `enhancement`.

        ## Note
        --------------
        Arguments for `background` is requires `background_size`, which is only available only two sizes `1920x1080` and `1280x720`.

        ## Short Example
        --------------

        More examples are available on our github: https://github.com/StawaDev/Estrapy-API/tree/main/Examples

        ```
        import Estrapy

        _player = {
            "player_1": "User_1",
            "player_2": "User_2",
        }

        _background = {
            "background_url": "https://xxx",
            "background_size": "1920x720",
        }

        async def shipper():
            x = await Estrapy.Games.shipper(players=_player, background=_background)
            x.save("Shipper.png")
        ```

        ## Arguments:
            - players: dict -- Set the player information
            - background: dict -- Set the background
        """

        _json = {"players": players, "background": background}
        req = post_api(route="games/shipper", json=_json)

        return Image.open(BytesIO(req.content))


class AniGames:
    @staticmethod
    async def truth(
        client: Optional[any] = None, generate: Optional[int] = None
    ) -> PropertiesManager:
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
        output = get_api(route=route)

        if client:
            _json = {
                "token_user": client.token_user,
                "user_id": client.user_id,
            }
            output = post_api(route=route, json=_json)

        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
            with_account=output.get("with_account"),
        )

        if generate:
            return await Base.produce(total=generate, route=route, type="text")

        return properties

    @staticmethod
    async def dare(
        client: Optional[any] = None, generate: Optional[int] = None
    ) -> PropertiesManager:
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
        output = get_api(route=route)

        if client:
            _json = {
                "token_user": client.token_user,
                "user_id": client.user_id,
            }
            output = post_api(route=route, json=_json)

        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
            with_account=output.get("with_account"),
        )

        if generate:
            return await Base.produce(total=generate, route=route, type="text")

        return properties

    @staticmethod
    async def waifu(client: Optional[any] = None) -> PropertiesManager:
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
        output = get_api(route=route)

        if client:
            _json = {
                "token_user": client.token_user,
                "user_id": client.user_id,
            }
            output = post_api(route=route, json=_json)

        properties = PropertiesManager(
            url=output.get("link"),
            type=output.get("type"),
            character_name=output.get("character_name"),
            total=output.get("total_image"),
            with_account=output.get("with_account"),
        )

        return properties

    @staticmethod
    async def husbando(client: Optional[any] = None) -> PropertiesManager:
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
        output = get_api(route=route)

        if client:
            _json = {
                "token_user": client.token_user,
                "user_id": client.user_id,
            }
            output = post_api(route=route, json=_json)

        properties = PropertiesManager(
            url=output.get("link"),
            type=output.get("type"),
            character_name=output.get("character_name"),
            total=output.get("total_image"),
            with_account=output.get("with_account"),
        )

        return properties

    @staticmethod
    async def shipper_waifu(
        client: Optional[any] = None, player: str = None
    ) -> PropertiesManager:
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
        output = get_api(route=route)

        if client:
            _json = {
                "token_user": client.token_user,
                "user_id": client.user_id,
            }
            output = post_api(route=route, json=_json)

        properties = PropertiesManager(
            player=output.get("player"),
            character_name=output.get("character_name"),
            percentage=output.get("percentage"),
            with_account=output.get("with_account"),
        )

        return properties

    @staticmethod
    async def shipper_husbando(
        client: Optional[any] = None, player: str = None
    ) -> PropertiesManager:
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
        output = get_api(route=route)

        if client:
            _json = {
                "token_user": client.token_user,
                "user_id": client.user_id,
            }
            output = post_api(route=route, json=_json)

        properties = PropertiesManager(
            player=output.get("player"),
            character_name=output.get("character_name"),
            percentage=output.get("percentage"),
            with_account=output.get("with_account"),
        )

        return properties
