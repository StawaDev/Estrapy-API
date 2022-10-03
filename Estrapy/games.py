from .http import get_api, BASE_URL
from .base import Base, ObjectConverter
from .property import PropertiesManager
from typing import Union, Optional
from io import BytesIO
from PIL import Image
import requests

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
    async def shipper(
        player: Optional[str],
        player2: Optional[str],
        player_image: Union[str, bytes] = None,
        player2_image: Union[str, bytes] = None,
        background_image: Union[str, bytes] = None,
        background_size: Optional[tuple] = None,
    ):
        """
        Description
        --------------
        A Function That Will Return an Edited Image with customized Background and Player Image.
        Currently, for the customized image like player_image still using a url. And also, for the background image default size is `1920x1080`.
        There's 2 available size for custom background picture, `1920x1080` and `1280x720`.
        In case you don't want to add an custom background or a player image, you can add `None` to the parameter value.

        How to use shipper (image) function (Examples)
        ----------------------------

        ```
        async def shipper():
            test = await Estrapy.Games.shipper(player="Player1", player2="Player2", player_image="None", player2_image="None", background="None", background_size="None")
            test.show()
        ```

        :param player
        :type player: Optional[str]
        :param player2
        :type player2: Optional[str]
        :param player_image
        :type player_image: Union[str, bytes]
        :param player_image2
        :type player_image2: Union[str, bytes]
        :param background_image
        :type background_image: Union[str, bytes]
        :param background_size
        :type background_size: Optional[str]
        """
        url = f"{BASE_URL}/games/shipper/image/?player={player}&player2={player2}&player_image={player_image}&player2_image={player2_image}&background={background_image}"
        if background_size is None:
            req = requests.get(url)
        if background_size is not None:
            size = f"{background_size[0]}x{background_size[1]}"
            req = requests.get(f"{url}&background_size={size}")

        a = Image.open(BytesIO(req.content))
        return a


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
