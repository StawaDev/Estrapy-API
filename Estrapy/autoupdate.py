import os
from .http import Requester
from packaging import version
from .__init__ import __version__

__all__ = ("AutoUpdate",)


class AutoUpdate:
    """An autoupdate with a reminder function that can be used to update and remind the user to use the client's most recent version."""

    def __init__(self):
        self.requester = Requester(custom_url="https://estra-api.vercel.app/version/")

    def update(self) -> None:
        """When the current version is on the previous version, the function will be called."""

        req = self.requester.post_api(json={"language": "python"})

        if version.parse(__version__) == version.parse(req.get("version")):
            return

        if version.parse(__version__) < version.parse(req.get("version")):
            os.system("pip install Estrapy-API --upgrade")

    def reminder(self) -> str:
        """This function will remind the user when there's a new version.

        Returns
        --------
        str
            If there's a new version, it will return str; otherwise, `None`.
        """

        req = self.requester.post_api(json={"language": "python"})

        if version.parse(__version__) == version.parse(req.get("version")):
            return

        if version.parse(__version__) < version.parse(req.get("version")):
            return f"[ Reminder ] Estrapy: A newer version of Estrapy is available ({req.get('version')})."
