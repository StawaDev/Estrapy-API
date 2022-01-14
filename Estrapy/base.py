import json
from pygments import highlight, lexers, formatters
from .http import get_api


class Base:
    async def JSONFormatter(JSONData):
        DATA = json.dumps(JSONData, indent=6, sort_keys=True)
        LISTING_DATA = highlight(
            DATA, lexers.JsonLexer(), formatters.TerminalFormatter()
        )
        return LISTING_DATA

    async def produce(total: int, full_url: str, type: str) -> None:
        if int(total) > 10:
            return "Estrapy Can't Produce More Than 10 Requests"
        if int(total) == 1:
            return "Estrapy Can't Produce Only 1 Request"
        LIST_URL = []
        for _ in range(int(total)):
            url = get_api(full_url)[f"{type}"]
            LIST_URL.append(url)
        return LIST_URL
