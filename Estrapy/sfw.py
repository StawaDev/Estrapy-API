import requests
import json


def main_api(user_requests):
    get_api = requests.get(
        f"https://estra-api.herokuapp.com/api/sfw/{user_requests}"
    ).json()
    if get_api != "<Response [503]>":
        api_dumps = json.dumps(get_api)
        return api_dumps
    else:
        api_down = "We might have a problem with the API, Please wait for it to be available"
        return api_down


class sfw:
    def run():
        run_link = json.loads(main_api("run"))["link"]
        return run_link

    def hug():
        hug_link = json.loads(main_api("hug"))["link"]
        return hug_link

    def smile():
        smile_link = json.loads(main_api("smile"))["link"]
        return smile_link

    def headpat():
        headpat_link = json.loads(main_api("headpat"))["link"]
        return headpat_link
