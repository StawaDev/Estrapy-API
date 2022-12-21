from typing import Union

__all__ = (
    "PropertiesManager",
    "OsuProfileProperties",
    "OsuBeatmapProperties",
)


class PropertiesManager(object):
    def __init__(self, **kwargs) -> None:
        self.url = kwargs.get("url")
        self.text = kwargs.get("text")
        self.type = kwargs.get("type")
        self.player = kwargs.get("player")
        self.character_name = kwargs.get("character_name")
        self.percentage = kwargs.get("percentage")
        self.total = kwargs.get("total")
        self.with_account = kwargs.get("with_account")
        self.original_response = kwargs.get("original_response")

    @property
    def url(self) -> Union[str, list[str]]:
        return self._url

    @url.setter
    def url(self, value) -> None:
        self._url = value

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value) -> None:
        self._text = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value) -> None:
        self._type = value

    @property
    def player(self) -> str:
        return self._player

    @type.setter
    def player(self, value) -> None:
        self._player = value

    @property
    def character_name(self) -> str:
        return self._character_name

    @character_name.setter
    def character_name(self, value) -> None:
        self._character_name = value

    @property
    def percentage(self) -> str:
        return self._percentage

    @percentage.setter
    def percentage(self, value) -> None:
        self._percentage = value

    @property
    def total(self) -> str:
        return self._total

    @total.setter
    def total(self, value) -> None:
        self._total = value

    @property
    def with_account(self) -> bool:
        return self._with_account

    @with_account.setter
    def with_account(self, value) -> None:
        self._with_account = value

    @property
    def original_response(self) -> dict:
        return self._original_response

    @original_response.setter
    def original_response(self, value) -> None:
        self._original_response = value


class AccountProperties(object):
    def __init__(self, **kwargs) -> None:
        self.username = kwargs.get("username")
        self.user_id = kwargs.get("user_id")
        self.client_id = kwargs.get("client_id")
        self.client_secret = kwargs.get("client_secret")

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value) -> None:
        self._username = value

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, value) -> None:
        self._user_id = value

    @property
    def client_id(self) -> str:
        return self._client_id

    @client_id.setter
    def client_id(self, value) -> None:
        self._client_id = value

    @property
    def client_secret(self) -> str:
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value) -> None:
        self._client_secret = value


class AccountStatistics(object):
    def __init__(self, **kwargs):
        self.sfw = kwargs.get("sfw")
        self.nsfw = kwargs.get("nsfw")
        self.games = kwargs.get("games")
        self.anigames = kwargs.get("anigames")
        self.osu = kwargs.get("osu")
        self.total_requests_user = kwargs.get("total_requests_user")

    @property
    def sfw(self) -> dict:
        return self._sfw

    @sfw.setter
    def sfw(self, value) -> None:
        self._sfw = value

    @property
    def nsfw(self) -> dict:
        return self._nsfw

    @nsfw.setter
    def nsfw(self, value) -> None:
        self._nsfw = value

    @property
    def games(self) -> dict:
        return self._games

    @games.setter
    def games(self, value) -> None:
        self._games = value

    @property
    def anigames(self) -> dict:
        return self._anigames

    @anigames.setter
    def anigames(self, value) -> None:
        self._anigames = value

    @property
    def osu(self) -> dict:
        return self._osu

    @osu.setter
    def osu(self, value) -> None:
        self._osu = value

    @property
    def total_requests_user(self) -> int:
        return self._total_requests_user

    @total_requests_user.setter
    def total_requests_user(self, value) -> None:
        self._total_requests_user = value


class OsuProfileProperties(object):
    __slots__ = (
        "avatar_url",
        "country_code",
        "default_group",
        "id",
        "is_active",
        "is_bot",
        "is_deleted",
        "is_online",
        "is_supporter",
        "last_visit",
        "pm_friends_only",
        "profile_colour",
        "username",
        "cover_url",
        "discord",
        "has_supported",
        "interests",
        "join_date",
        "kudosu",
        "location",
        "max_blocks",
        "max_friends",
        "occupation",
        "playmode",
        "playstyle",
        "post_count",
        "profile_order",
        "title",
        "title_url",
        "twitter",
        "website",
        "country",
        "cover",
        "account_history",
        "active_tournament_banner",
        "badges",
        "beatmap_playcounts_count",
        "comments_count",
        "favourite_beatmapset_count",
        "follower_count",
        "graveyard_beatmapset_count",
        "groups",
        "guest_beatmapset_count",
        "loved_beatmapset_count",
        "mapping_follower_count",
        "monthly_playcounts",
        "nominated_beatmapset_count",
        "page",
        "pending_beatmapset_count",
        "previous_usernames",
        "rank_highest",
        "ranked_beatmapset_count",
        "replays_watched_counts",
        "scores_best_count",
        "scores_first_count",
        "scores_pinned_count",
        "scores_recent_count",
        "statistics",
        "support_level",
        "user_achievements",
        "rank_history",
        "rankHistory",
        "ranked_and_approved_beatmapset_count",
        "unranked_beatmapset_count",
    )

    def __init__(self, _json: dict = None) -> None:
        if _json:
            for key, value in _json.items():
                setattr(self, key, value)


class OsuBeatmapProperties(object):
    __slots__ = (
        "beatmapset_id",
        "difficulty_rating",
        "id",
        "mode",
        "status",
        "total_length",
        "user_id",
        "version",
        "accuracy",
        "ar",
        "bpm",
        "convert",
        "count_circles",
        "count_sliders",
        "count_spinners",
        "cs",
        "deleted_at",
        "drain",
        "hit_length",
        "is_scoreable",
        "last_updated",
        "mode_int",
        "passcount",
        "playcount",
        "ranked",
        "url",
        "checksum",
        "beatmapset",
        "failtimes",
        "max_combo",
    )

    def __init__(self, _json: dict = None) -> None:
        if _json:
            for key, value in _json.items():
                setattr(self, key, value)
