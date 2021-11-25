import requests
import json


def main_api(user_requests):
    get_api = requests.get(
        f"https://estra-api.herokuapp.com/api/sfw/{user_requests}"
    ).json()
    api_dumps = json.dumps(get_api)
    return api_dumps


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
        headpat_link = json.loads(main_api("headpat")["link"])
        return headpat_link
