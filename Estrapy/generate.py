from .http import get_api


def generate(total: int, full_url: str, type: str) -> None:
    LIST_URL = []
    for _ in range(total):
        url = get_api(full_url)[f"{type}"]
        LIST_URL.append(url)
    return LIST_URL
