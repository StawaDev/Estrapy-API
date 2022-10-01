from typing import Optional


class PropertiesManager(object):
    def __init__(
        self,
        url: str,
        text: Optional[str],
        type: Optional[str],
        player: Optional[str],
        character_name: Optional[str],
        percentage: Optional[str],
    ):
        self.url = url
        self.text = text
        self.type = type
        self.player = player
        self.character_name = character_name
        self.percentage = percentage

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def player(self):
        return self._player

    @type.setter
    def player(self, value):
        self._player = value

    @property
    def character_name(self):
        return self._character_name

    @character_name.setter
    def character_name(self, value):
        self._character_name = value

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        self._percentage = value
