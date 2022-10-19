__all__ = (
    "PropertiesManager",
    "OsuProfileProperties",
    "OsuBeatmapProperties",
)


class PropertiesManager(object):
    def __init__(self, *args, **kwargs) -> None:
        self.url = kwargs.get("url")
        self.text = kwargs.get("text")
        self.type = kwargs.get("type")
        self.player = kwargs.get("player")
        self.character_name = kwargs.get("character_name")
        self.percentage = kwargs.get("percentage")
        self.total = kwargs.get("total")
        self.with_account = kwargs.get("with_account")

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

    @property
    def with_account(self) -> bool:
        return self._with_account

    @with_account.setter
    def with_account(self, value):
        self._with_account = value


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
        "page",
        "pending_beatmapset_count",
        "previous_usernames",
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

    def __init__(self, _json: dict = None):
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

    def __init__(self, _json: dict = None):
        if _json:
            for key, value in _json.items():
                setattr(self, key, value)
