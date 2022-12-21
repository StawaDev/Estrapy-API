import json.decoder
import requests
from .errors import APIOffline, InvalidStatusCode, InvalidResponse


class Requester:
    __all__ = ("base_url", "get_api", "post_api", "post_response")

    def __init__(self, **kwargs):
        self.base_url = "https://estra-api.vercel.app/api/v1/"
        self.custom_url = kwargs.get("custom_url")

        if self.custom_url:
            self.base_url = self.custom_url

    def get_api(self, route: str = None) -> dict:
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
