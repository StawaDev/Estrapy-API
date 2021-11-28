__all__ = ("APIOffline", "InvalidResponse", "InvalidStatusCode")


class APIOffline(Exception):
    """
    Raised when the Estrapy API is offline.
    """


class InvalidStatusCode(Exception):
    """
    Raised when the Estrapy API returns an invalid status code.
    """


class InvalidResponse(Exception):
    """
    Raised when the Estrapy API returns an invalid response.
    """
