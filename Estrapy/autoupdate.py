import requests
import os

version = requests.get("https://estra-api.herokuapp.com/").json()["Version"]


def autoupdate():
    if version != "0.1.6":
        print(
            f"Estrapy-API - new version is up! AutoUpdate will be upgrading version to {version}"
        )
        os.system(f"pip install Estrapy-API=={version}")
    else:
        print("No need to update")


autoupdate()
