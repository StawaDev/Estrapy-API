from .http import Requester
from .errors import InvalidNumber
from typing import Optional
from pygments import highlight, lexers, formatters
import json
import requests

__all__ = ("Base", "ObjectConverter")


class Base:
    def __init__(self):
        self.requester = Requester()

    def json_beautifier(self, data) -> any:
        """
        This function only can be used by the CLI.
        """

        _json = json.dumps(data, indent=6, sort_keys=True)
        beautifier = highlight(
            _json, lexers.JsonLexer(), formatters.TerminalFormatter()
        )
        return beautifier

    async def produce(self, total: int, route: str, type: str = "link") -> list:
        """
        Returns a list of responses for the given route.
        """

        generated_urls = []

        if total > 15 or total < 2:
            raise InvalidNumber(
                "Can't generate more than 15 or less than 1 request at a time."
            )

        for _ in range(int(total)):
            url = self.requester.get_api(route=route).get(type)
            generated_urls.append(url)

        return generated_urls

    async def save(
        self,
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
            - category: str -- Target to download, (ex. sfw/hug)
            - total: Optional[int] -- Total of image to download, default is 1
            - filename: Optional[str] -- Filename to save, default is target category with number behind it.
        """

        url_list = []
        file_list = []

        if total > 15 or total < 1:
            raise InvalidNumber(
                "Can't generate more than 15 or less than 1 request at a time."
            )

        if total == 1:
            req = self.requester.get_api(route=category)
            link = req.get("link")
            _filename = f"{filename if filename else category.split('/')[1].title()}.{req.get('type')}"

            with open(_filename, "wb") as f:
                f.write(requests.get(link).content)

            return [_filename, link]

        for i in range(0, int(total)):
            req = self.requester.get_api(route=category)
            link = req.get("link")
            _filename = f"{filename}_{i+1}.{req.get('type')}"

            if not (_filename):
                _filename = f"{category.split('/')[1].title()}_{i+1}.{req.get('type')}"

            url_list.append(link)
            file_list.append(_filename)

            with open(_filename, "wb") as f:
                f.write(requests.get(link).content)

        return [url_list, file_list]
