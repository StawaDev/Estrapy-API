__all__ = ("PropertiesManager",)


class PropertiesManager(object):
    def __init__(self, *args, **kwargs) -> None:
        self.url = kwargs.get("url")
        self.text = kwargs.get("text")
        self.type = kwargs.get("type")
        self.player = kwargs.get("player")
        self.character_name = kwargs.get("character_name")
        self.percentage = kwargs.get("percentage")
        self.total = kwargs.get("total")

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

    @property
    def total(self) -> str:
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
