import json
from pygments import highlight, lexers, formatters


def JSONFormatter(JSONData):
    DATA = json.dumps(JSONData, indent=6, sort_keys=True)
    LISTING_DATA = highlight(DATA, lexers.JsonLexer(), formatters.TerminalFormatter())
    return LISTING_DATA
