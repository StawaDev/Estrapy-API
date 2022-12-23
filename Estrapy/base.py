from .http import Requester
from .errors import InvalidNumber, InvalidResponse
from typing import Optional, Tuple, Union
import requests

__all__ = ("Base", "ObjectConverter")


class Base:
    """The base class is an important one for Estrapy-API because it can be used to save and generate many requests."""

    def __init__(self):
        self.requester = Requester()

    async def produce(
        self, total: int, route: str, type: str = "link", **kwargs
    ) -> Union[list[str], Tuple[list[str], bool]]:
        """This function will return as Union[list[str], Tuple[list[str], bool]]

        Parameters
        -----------
        total: int
            Total requests to the API
        route: str
            Route to the API
        type:
            Obtain results from JSON keys
        """

        generated_urls = []
        with_account = False
        if total > 15 or total < 2:
            raise InvalidNumber(
                "Can't generate more than 15 or less than 1 request at a time."
            )

        _json = kwargs.get("json")
        for _ in range(int(total)):
            if _json:
                url = self.requester.post_api(route=route, json=_json)
                with_account = True
                error = url.get("error")

                if error:
                    raise InvalidResponse(
                        f"There might be an error with your client_id or client_secret. Error reason: {error}"
                    )

                generated_urls.append(url)

            if not _json:
                url = self.requester.get_api(route=route).get(type)
                generated_urls.append(url)

        return generated_urls if not _json else generated_urls, with_account

    async def save(
        self,
        category: str = None,
        total: Optional[int] = 1,
        filename: Optional[str] = None,
    ) -> list:
        """This function will save image from specified category.
        Filename is optional, if not provided, it will be saved as target index 1 with number behind it.

        Parameters
        -----------
        category: str
            Target to download, (ex. sfw/hug)
        total: Optional[int]
            Total of image to download, default is 1
        filename: Optional[str]
            Filename to save, default is target category with number behind it.
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
