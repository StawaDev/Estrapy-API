import json
from pygments import highlight, lexers, formatters
from .http import get_api

class Base:
    def JSONFormatter(JSONData):
        DATA = json.dumps(JSONData, indent=6, sort_keys=True)
        LISTING_DATA = highlight(DATA, lexers.JsonLexer(), formatters.TerminalFormatter())
        return LISTING_DATA

    def produce(total: int, full_url: str, type: str) -> None:
        if total > 10:
            return "Estrapy Can't Produce More Than 10 Requests"
        LIST_URL = []
        for _ in range(total):
            url = get_api(full_url)[f"{type}"]
            LIST_URL.append(url)
        return LIST_URL
