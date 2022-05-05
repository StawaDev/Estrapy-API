import json
from typing import Optional, Tuple
from pygments import highlight, lexers, formatters
from .http import get_api, BASE_URL
import requests

__all__ = "Base"


class Base:
    async def JSONFormatter(JSONData):
        DATA = json.dumps(JSONData, indent=6, sort_keys=True)
        LISTING_DATA = highlight(
            DATA, lexers.JsonLexer(), formatters.TerminalFormatter()
        )
        return LISTING_DATA

    async def produce(total: int, full_url: str, type: str) -> None:
        if int(total) > 10:
            return "Estrapy can't produce more than 10 requests in once."
        if int(total) == 1:
            return "Estrapy can't produce only 1 request, needed more than 1 request."
        LIST_URL = []
        for _ in range(int(total)):
            url = get_api(full_url)[f"{type}"]
            LIST_URL.append(url)
        return LIST_URL

    async def save(
        target: Optional[Tuple[str, str]] = None,
        total: Optional[int] = 1,
        filename: Optional[str] = None,
    ) -> None:
        """
        Description
        --------------
        A Function That Will Download an Image from Estra-API.
        Filename is optional, if not provided, it will be saved as target index 1 with number behind it.

        How to use smile function (Examples)
        ----------------------------
        ```
        from Estrapy.base import Base

        async def smile():
            await Base.save(target=("sfw", "hug"), filename="Hug") # Will save a hug gif

        async def smile_total():
            await Base.save(target=("sfw", "smile"), total=3, filename="SmileGif") # Will save 3 smile gifs with number behind its filename
        ```

        :param target
        :type tuple
        :param total
        :type int
        :param filename
        :type str
        """

        url = requests.get(f"{BASE_URL}{target[0]}/{target[1]}").json()
        links = url["link"]
        _filename = f"{filename}.{url['type']}"

        i = 0
        fileList = []
        urlList = []

        if int(total) < 1:
            return "Estrapy can't produce only 1 request, needed more than 1 request."

        if int(total) > 10:
            return "Estrapy can't produce more than 10 requests in once."

        if int(total) == 1:
            with open(_filename, "wb") as f:
                f.write(requests.get(links).content)
            return [_filename, links]

        for _ in range(int(total)):
            _url = requests.get(f"{BASE_URL}{target[0]}/{target[1]}").json()
            _links = _url["link"]
            _filename = f"{filename}{i}.{url['type']}".replace("0", "")

            if filename is None:
                _filename = f"{target[-1]}{i}.{url['type']}".replace("0", "")

            fileList.append(_filename)
            urlList.append(_links)

            with open(_filename, "wb") as f:
                f.write(requests.get(_links).content)

            i += 1

        return [fileList, urlList]
