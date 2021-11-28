import requests
import json
from errors import *

def main_api(user_requests):
    try:
        get_api = requests.get(
            f"https://estra-api.herokuapp.com/api/sfw/{user_requests}"
        ).json()
        if get_api != "<Response [503]>":
            api_dumps = json.dumps(get_api)
            return api_dumps
    except:
        return api_down


class sfw:
    def run():
        "A Function That Will Return a SFW Run GIF"
        try:
            run_link = json.loads(main_api("run"))["link"]
            return run_link
        except:
            return api_down

    def hug():
        "A Function That Will Return a SFW Hug GIF"
        try:
            hug_link = json.loads(main_api("hug"))["link"]
            return hug_link
        except:
            return errors.api_down

    def smile():
        "A Function That Will Return a SFW Smile GIF"
        try:
            smile_link = json.loads(main_api("smile"))["link"]
            return smile_link
        except:
            return errors.api_down

    def headpat():
        "A Function That Will Return a SFW Headpat GIF"
        try:
            headpat_link = json.loads(main_api("headpat"))["link"]
            return headpat_link
        except:
            return errors.api_down

    def poke():  # Not Implemented Yet!
        try:
            poke_link = json.loads(main_api("poke"))["link"]
            return poke_link
        except:
            return errors.api_down

    def bite():  # Not Implemented Yet!
        try:
            bite_link = json.loads(main_api("bite"))["link"]
            return bite_link
        except:
            return errors.api_down

    def neko():  # Not Implemented Yet!
        try:
            neko_link = json.loads(main_api("neko"))["link"]
            return neko_link
        except:
            api_down = "We might have a problem with the API, Please wait for it to be available"
            return api_down
