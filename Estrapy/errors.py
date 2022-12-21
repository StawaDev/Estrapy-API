__all__ = (
    "APIOffline",
    "InvalidResponse",
    "InvalidStatusCode",
    "InvalidNumber",
)


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


class InvalidNumber(Exception):
    """
    When the Estrapy's function returns an invalid number, this exception is raised.
    """
