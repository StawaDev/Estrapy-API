from .http import get_api, post_api
from .base import Base, ObjectConverter
from .property import PropertiesManager
from typing import Optional
from io import BytesIO
from PIL import Image

__all__ = (
    "Games",
    "AniGames",
)

Converter = ObjectConverter()


class Games:
    @staticmethod
    async def truth(generate: Optional[int] = None) -> PropertiesManager:
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
        output = get_api(route=route)
        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
        )

        if generate:
            return await Base.produce(total=generate, route=route, type="text")

        return properties

    @staticmethod
    async def dare(generate: Optional[int] = None) -> PropertiesManager:
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
            - generate: int -- Generate how many requests to return
        """

        route = "games/dare"
        output = get_api(route=route)
        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
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
    async def truth(generate: Optional[int] = None) -> PropertiesManager:
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
            - generate: int -- Generate how many requests to return
        """

        route = "anigames/truth"
        output = get_api(route=route)
        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
        )

        if generate:
            return await Base.produce(total=generate, route=route, type="text")

        return properties

    @staticmethod
    async def dare(generate: Optional[int] = None) -> PropertiesManager:
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
            - generate: int -- Generate how many requests to return
        """

        route = "anigames/dare"
        output = get_api(route=route)
        properties = PropertiesManager(
            text=output.get("text"),
            type=output.get("type"),
            total=output.get("total_text"),
        )

        if generate:
            return await Base.produce(total=generate, route=route, type="text")

        return properties

    @staticmethod
    async def waifu() -> PropertiesManager:
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
        """

        route = "anigames/waifu"
        output = get_api(route=route)
        properties = PropertiesManager(
            url=output.get("link"),
            type=output.get("type"),
            character_name=output.get("character_name"),
            total=output.get("total_image"),
        )

        return properties

    @staticmethod
    async def husbando() -> PropertiesManager:
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
        """

        route = "anigames/husbando"
        output = get_api(route=route)
        properties = PropertiesManager(
            url=output.get("link"),
            type=output.get("type"),
            character_name=output.get("character_name"),
            total=output.get("total_image"),
        )

        return properties

    @staticmethod
    async def shipper_waifu(player: str) -> PropertiesManager:
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
        properties = PropertiesManager(
            player=output.get("player"),
            character_name=output.get("character_name"),
            percentage=output.get("percentage"),
        )

        return properties

    @staticmethod
    async def shipper_husbando(player: str) -> PropertiesManager:
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
        properties = PropertiesManager(
            player=output.get("player"),
            character_name=output.get("character_name"),
            percentage=output.get("percentage"),
        )

        return properties
