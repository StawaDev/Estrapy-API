import json.decoder
import requests
from .errors import APIOffline, InvalidStatusCode, InvalidResponse

__all__ = ("BASE_URL", "get_api")

BASE_URL = "https://estra-api.vercel.app/api/v1/"


def get_api(route: str) -> dict:
    r = None

    try:
        r = requests.get(BASE_URL + route)

        if not 200 <= r.status_code < 300:
            raise InvalidStatusCode(f"{route} returned {r.status_code}")

        return r.json()
    except json.decoder.JSONDecodeError:
        raise InvalidResponse(f"Excected JSON from API but received {r.text}")
    except requests.exceptions.ConnectionError:
        raise APIOffline("The Estrapy API is offline.")


def post_api(route: str, json: any) -> dict:
    r = None

    try:
        r = requests.post(url=BASE_URL + route, json=json)

        if not 200 <= r.status_code < 300:
            raise InvalidStatusCode(f"{route} returned {r.status_code}")

        return r.json()
    except json.decoder.JSONDecodeError:
        raise InvalidResponse(f"Excected JSON from API but received {r.text}")
    except requests.exceptions.ConnectionError:
        raise APIOffline("The Estrapy API is offline.")
