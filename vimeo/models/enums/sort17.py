from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort17(str, Enum):
    ADDED = "added"
    ALPHABETICAL = "alphabetical"
    ARRANGED = "arranged"
    COMMENTS = "comments"
    DATE = "date"
    DURATION = "duration"
    LIKES = "likes"
    PLAYS = "plays"

    __str__ = str.__str__


Sort17OrStr: TypeAlias = Annotated[Sort17 | str, open_enum_validator(Sort17)]
