import json.decoder
import requests
from .errors import APIOffline, InvalidStatusCode, InvalidResponse


class Requester:
    """This class has functions that can get or send requests to the API.

    Parameters
    -----------
    custom_url: str
        A custom URL to fetch another API
    """

    __all__ = ("base_url", "get_api", "post_api", "post_response")

    def __init__(self, **kwargs):
        self.base_url = "https://estra-api.vercel.app/api/v1/"
        self.custom_url = kwargs.get("custom_url")

        if self.custom_url:
            self.base_url = self.custom_url

    def get_api(self, route: str = None) -> dict:
        """Get a response from a specific route to the API.

        Parameters
        -----------
        route: str
            Route to the API
        """

        r = None

        try:
            r = requests.get(url=self.base_url if not route else self.base_url + route)

            if not 200 <= r.status_code < 300:
                raise InvalidStatusCode(f"{route} returned {r.status_code}")

            return r.json()
        except json.decoder.JSONDecodeError:
            raise InvalidResponse(f"Excected JSON from API but received {r.text}")
        except requests.exceptions.ConnectionError:
            raise APIOffline("The Estrapy API is offline.")

    def post_api(self, route: str = None, json=None) -> dict:
        """Send a request and get a response from a specific route to the API.

        Parameters
        -----------
        route: str
            Route to the API
        json: dict
            The API receives JSON data.
        """

        r = None

        try:
            r = requests.post(
                url=self.base_url if not route else self.base_url + route,
                json=json,
            )

            if not 200 <= r.status_code < 300:
                raise InvalidStatusCode(f"{route} returned {r.status_code}")

            return r.json()
        except json.decoder.JSONDecodeError:
            raise InvalidResponse(f"Excected JSON from API but received {r.text}")
        except requests.exceptions.ConnectionError:
            raise APIOffline("The Estrapy API is offline.")

    def post_response(self, route: str = None, json=None) -> requests.Response:
        """Send a request and get a response from a specific route to the API.

        Parameters
        -----------
        route: str
            Route to the API
        json: dict
            The API receives JSON data.
        """

        r = None

        try:
            r = requests.post(
                url=self.base_url if not route else self.base_url + route,
                json=json,
            )

            if not 200 <= r.status_code < 300:
                raise InvalidStatusCode(f"{route} returned {r.status_code}")

            return r
        except json.decoder.JSONDecodeError:
            raise InvalidResponse(f"Excected JSON from API but received {r.text}")
        except requests.exceptions.ConnectionError:
            raise APIOffline("The Estrapy API is offline.")
