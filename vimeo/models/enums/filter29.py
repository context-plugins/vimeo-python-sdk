from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter29(str, Enum):
    ALL = "all"
    BUY = "buy"
    EXPIRING_SOON = "expiring_soon"
    EXTRA = "extra"
    MAIN = "main"
    MAIN_VIEWABLE = "main.viewable"
    RENT = "rent"
    TRAILER = "trailer"
    UNWATCHED = "unwatched"
    VIEWABLE = "viewable"
    WATCHED = "watched"

    __str__ = str.__str__


Filter29OrStr: TypeAlias = Annotated[Filter29 | str, open_enum_validator(Filter29)]
