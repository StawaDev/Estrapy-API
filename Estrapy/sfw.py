import requests
import json


def main_api(user_requests):
    try:
        get_api = requests.get(
            f"https://estra-api.herokuapp.com/api/sfw/{user_requests}"
        ).json()
        if get_api != "<Response [503]>":
            api_dumps = json.dumps(get_api)
            return api_dumps
    except:
        api_down = "We might have a problem with the API, Please wait for it to be available"
        return api_down


class sfw:
    def run():
        try:
            run_link = json.loads(main_api("run"))["link"]
            return run_link
        except:
            api_down = "We might have a problem with the API, Please wait for it to be available"
            return api_down

    def hug():
        try:
            hug_link = json.loads(main_api("hug"))["link"]
            return hug_link
        except:
            api_down = "We might have a problem with the API, Please wait for it to be available"
            return api_down

    def smile():
        try:
            smile_link = json.loads(main_api("smile"))["link"]
            return smile_link
        except:
            api_down = "We might have a problem with the API, Please wait for it to be available"
            return api_down

    def headpat():
        try:
            headpat_link = json.loads(main_api("headpat"))["link"]
            return headpat_link
        except:
            api_down = "We might have a problem with the API, Please wait for it to be available"
            return api_down

    def poke(): # Not Available Yet!
        try:
            poke_link = json.loads(main_api("poke"))["link"]
            return poke_link
        except:
            api_down = "We might have a problem with the API, Please wait for it to be available"
            return api_down
        
    def bite(): # Not Available Yet!
        try:
            bite_link = json.loads(main_api("bite"))["link"]
            return bite_link
        except:
            api_down = "We might have a problem with the API, Please wait for it to be available"
            return api_down