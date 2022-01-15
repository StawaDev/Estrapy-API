from typing import Optional
import requests
import os
from .__init__ import __version__ as current_version

version = requests.get("https://estra-api.herokuapp.com/version/").json()["Estrapy-API"][
    "Estrapy Version"
]
change_log = requests.get("https://estra-api.herokuapp.com/version/").json()["Estrapy-API"][
    "Change Logs"
]


class AutoUpdate:
    def __init__(self, output: bool = False, change_log: bool = False) -> None:
        self.output = output
        self.change_log = change_log


    def updater():
        if current_version != version:
            print(f"Estrapy-API - new version is up! AutoUpdate will be upgrading version to {version}")
            os.system(f"pip install Estrapy-API=={version}")
        print("Estrapy-API - No need to update")


    def update(self):
        if self.output and self.change_log:
            AutoUpdate.updater()
            print(f"Estrapy Changelog - {change_log}")
            return

        if self.output:
            AutoUpdate.updater()
            return

        if self.change_log:
            print(f"Estrapy Changelog - {change_log}")
            return
