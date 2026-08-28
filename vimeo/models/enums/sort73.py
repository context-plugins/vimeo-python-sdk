from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort73(str, Enum):
    ALPHABETICAL = "alphabetical"
    COMMENTS = "comments"
    DATE = "date"
    DURATION = "duration"
    LIKES = "likes"
    PLAYS = "plays"
    RELEVANT = "relevant"

    __str__ = str.__str__


Sort73OrStr: TypeAlias = Annotated[Sort73 | str, open_enum_validator(Sort73)]
