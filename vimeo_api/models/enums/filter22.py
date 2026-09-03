from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter22(str, Enum):
    APP_ONLY = "app_only"
    COLD_PRIVACY = "cold_privacy"
    COLD_STORAGE = "cold_storage"
    EMBEDDABLE = "embeddable"
    FEATURED = "featured"
    LIVE = "live"
    NO_PLACEHOLDER = "no_placeholder"
    NOLIVE = "nolive"
    PLAYABLE = "playable"
    SCREEN_RECORDED = "screen_recorded"

    __str__ = str.__str__


Filter22OrStr: TypeAlias = Annotated[Filter22 | str, open_enum_validator(Filter22)]
