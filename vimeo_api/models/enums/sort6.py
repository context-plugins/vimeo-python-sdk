from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort6(str, Enum):
    ALPHABETICAL = "alphabetical"
    COMMENTS = "comments"
    DATE = "date"
    DURATION = "duration"
    FEATURED = "featured"
    LIKES = "likes"
    PLAYS = "plays"
    RELEVANT = "relevant"

    __str__ = str.__str__


Sort6OrStr: TypeAlias = Annotated[Sort6 | str, open_enum_validator(Sort6)]
