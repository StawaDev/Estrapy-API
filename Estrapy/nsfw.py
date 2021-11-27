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
    
class nsfw:
    def kill(): # Not Available Yet!
        try:
            kill_link = json.loads(main_api("kill"))["link"]
            return kill_link
        except:
            api_down = "We might have a problem with the API, Please wait for it to be available"
            return api_down