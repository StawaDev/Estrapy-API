import requests
import json


def main_api(user_requests):
    get_api = requests.get(
        f"https://estra-api.herokuapp.com/api/sfw/{user_requests}"
    ).json()
    return get_api


def run():
    run_link = json.loads(main_api("run"))
    return run_link


def hug():
    hug_link = json.loads(main_api("hug"))
    return hug_link


def smile():
    smile_link = json.loads(main_api("smile"))
    return smile_link


def headpat():
    headpat_link = json.loads(main_api("headpat"))
    return headpat_link
