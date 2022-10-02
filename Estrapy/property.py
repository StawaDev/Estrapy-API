__all__ = ("PropertiesManager",)


class PropertiesManager(object):
    def __init__(
        self,
        url: str = None,
        text: str = None,
        type: str = None,
        player: str = None,
        character_name: str = None,
        percentage: str = None,
    ) -> None:
        self.url = url
        self.text = text
        self.type = type
        self.player = player
        self.character_name = character_name
        self.percentage = percentage

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def player(self) -> str:
        return self._player

    @type.setter
    def player(self, value):
        self._player = value

    @property
    def character_name(self) -> str:
        return self._character_name

    @character_name.setter
    def character_name(self, value):
        self._character_name = value

    @property
    def percentage(self) -> str:
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        self._percentage = value
