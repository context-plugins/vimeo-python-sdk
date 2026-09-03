from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter19(str, Enum):
    ALL = "all"
    EXPIRING_SOON = "expiring_soon"
    FILM = "film"
    IMPORTANT = "important"
    PURCHASED = "purchased"
    RENTED = "rented"
    SERIES = "series"
    SUBSCRIPTION = "subscription"
    UNWATCHED = "unwatched"
    WATCHED = "watched"

    __str__ = str.__str__


Filter19OrStr: TypeAlias = Annotated[Filter19 | str, open_enum_validator(Filter19)]
