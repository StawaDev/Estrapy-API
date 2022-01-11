import requests
import os
from .__init__ import __version__ as current_version

version = requests.get("https://estra-api.herokuapp.com/version").json()["Estrapy-API"]["Estrapy Version"]


def autoupdate():
    if current_version != version:
        print(
            f"Estrapy-API - new version is up! AutoUpdate will be upgrading version to {version}"
        )
        os.system(f"pip install Estrapy-API=={version}")
    else:
        print("Estrapy-API - No need to update")


autoupdate()
