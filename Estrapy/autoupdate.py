from typing import Optional
import requests
import os
from .__init__ import __version__ as current_version

version = requests.get("https://estra-api.herokuapp.com/version/").json()[
    "Estrapy-API"
]["Estrapy Version"]
change_log = requests.get("https://estra-api.herokuapp.com/version/").json()[
    "Estrapy-API"
]["Change Logs"]


class AutoUpdate:
    def __init__(self, reminder: bool = True, auto: bool = False) -> None:
        self._reminder = reminder
        self.auto = auto

    def run(self):
        if self._reminder:
            return self.reminder()

        if self.auto:
            return self.auto_update()

    def reminder(self):
        """
        Reminding if there's a new compatible version
        """

        print(
            f"Estrapy-API - New version available {version}, please update your Estrapy-API. | Changelogs - {change_log}"
        )

    def auto_update(self):
        """
        Automaticly updating the Estrapy-API to the latest version
        """

        return self.console_update()

    def console_update():
        if current_version != version:
            print(
                f"Estrapy-API - Upgrading version to {version}, please wait... | Changelogs - {change_log}"
            )
            os.system(f"pip install Estrapy-API=={version}")
