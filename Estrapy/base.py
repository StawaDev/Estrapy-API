from .http import get_api
from .errors import InvalidNumber
from typing import Optional
from pygments import highlight, lexers, formatters
import json
import requests

__all__ = ("Base", "ObjectConverter")


class Base:
    def json_beautifier(data) -> any:
        """
        This function only can be used by the CLI.
        """

        _json = json.dumps(data, indent=6, sort_keys=True)
        beautifier = highlight(
            _json, lexers.JsonLexer(), formatters.TerminalFormatter()
        )
        return beautifier

    async def produce(total: int, route: str, type: str = "url") -> list:
        """
        Returns a list of responses for the given route.
        """

        generated_urls = []

        if total > 10 or total < 2:
            raise InvalidNumber(
                "Can't generate more than 10 or less than 1 request at a time."
            )

        for _ in range(int(total)):
            url = get_api(route=route).get(type)
            generated_urls.append(url)

        return generated_urls

    async def save(
        category: str = None,
        total: Optional[int] = 1,
        filename: Optional[str] = None,
    ) -> list:
        """
        ### Description
        --------------
        This function will save image from specified category.
        Filename is optional, if not provided, it will be saved as target index 1 with number behind it.

        ### How to use save function (Examples)
        ----------------------------
        ```
        import asyncio
        from Estrapy.base import Base

        async def save():
            await Base.save(target=("sfw/hug"), filename="Hug") # Will save a hug gif

        async def save_generated():
            await Base.save(target=("sfw/smile"), total=3, filename="SmileGif") # Will save 3 smile gifs with number behind its filename

        asyncio.run(save())
        asyncio.run(save_generated())
        ```

        ### Arguments:
            - target: str -- Target to download, (ex. sfw/hug)
            - total: Optional[int] -- Total of image to download, default is 1
            - filename: Optional[str] -- Filename to save, default is target category with number behind it.
        """

        if total > 10 or total < 1:
            raise InvalidNumber(
                "Can't generate more than 10 or less than 1 request at a time."
            )

        if total == 1:
            req = get_api(route=category)
            link = req.get("link")
            _filename = f"{filename if filename else category.split('/')[1].upper()}.{req.get('type')}"

            with open(_filename, "wb") as f:
                f.write(requests.get(link).content)

            return [_filename, link]

        for i in range(int(total)):
            url_list = []
            file_list = []

            req = get_api(route=category)
            link = req.get("link")
            _filename = f"{filename}_{i}.{req.get('type')}".replace("0", "1")

            if not (_filename):
                _filename = (
                    f"{category.split('/')[1].upper()}_{i}.{req.get('type')}".replace(
                        "0", "1"
                    )
                )

            url_list.append(link)
            file_list.get(_filename)

            with open(_filename, "wb") as f:
                f.write(requests.get(link).content)

            return [url_list, file_list]


class ObjectConverter:
    def __init__(self, **kwargs):
        self.json = kwargs
        for i in self.json.keys():
            setattr(self, i, self.json[i])

    @classmethod
    def convert_obj(cls, obj):
        x = json.loads(obj)
        return cls(**x)

    def __repr__(self):
        return f"{self.json}"
