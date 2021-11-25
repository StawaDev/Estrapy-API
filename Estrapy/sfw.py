import requests


def main_api(user_requests):
    get_api = requests.get(
        f"https://estra-api.herokuapp.com/api/sfw/{user_requests}"
    ).json()
    return get_api


def run():
    run_link = main_api("run")
    return run_link


def hug():
    hug_link = main_api("hug")
    return hug_link


def smile():
    smile_link = main_api("smile")
    return smile_link


def headpat():
    headpat_link = main_api("headpat")
    return headpat_link
