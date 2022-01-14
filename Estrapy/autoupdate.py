from typing import Optional
import requests
import os
from .__init__ import __version__ as current_version

version = requests.get("https://estra-api.herokuapp.com/version").json()["Estrapy-API"][
    "Estrapy Version"
]
change_log = requests.get("https://estra-api.heroku.com/version").json()["Estra-API"][
    "Estrapy Change Log"
]


class AutoUpdate:
    def __init__(self, output: bool = False, change_log: bool = False) -> None:
        self.output = output
        self.change_log = change_log

    def settings(self):
        if self.output:
            if current_version != version:
                print(
                    f"Estrapy-API - new version is up! AutoUpdate will be upgrading version to {version}"
                )
                os.system(f"pip install Estrapy-API=={version}")
            print("Estrapy-API - No need to update")

        if self.change_log:
            print(f"Estrapy CHangelog - {change_log}")
