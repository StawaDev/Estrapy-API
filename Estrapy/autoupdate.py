import requests
import os
from packaging import version
from .__init__ import __version__

__all__ = ("AutoUpdate",)


class AutoUpdate:
    def __init__(self):
        self.url = "https://estra-api.vercel.app/version/"

    def update(self):
        req = requests.post(url=self.url, json={"language": "python"}).json()

        if version.parse(__version__) == version.parse(req.get("version")):
            return

        if version.parse(__version__) < version.parse(req.get("version")):
            os.system("pip install Estrapy-API --upgrade")

    def reminder(self):
        req = requests.post(url=self.url, json={"language": "python"}).json()

        if version.parse(__version__) == version.parse(req.get("version")):
            return

        if version.parse(__version__) < version.parse(req.get("version")):
            return f"[ Reminder ] Estrapy: A newer version of Estrapy is available ({req.get('version')})."
