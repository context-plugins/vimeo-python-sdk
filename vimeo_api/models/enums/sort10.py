from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort10(str, Enum):
    ADDED = "added"
    ALPHABETICAL = "alphabetical"
    COMMENTS = "comments"
    DATE = "date"
    DEFAULT = "default"
    DURATION = "duration"
    LIKES = "likes"
    MANUAL = "manual"
    MODIFIED_TIME = "modified_time"
    PLAYS = "plays"

    __str__ = str.__str__


Sort10OrStr: TypeAlias = Annotated[Sort10 | str, open_enum_validator(Sort10)]
