from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort35(str, Enum):
    ALPHABETICAL = "alphabetical"
    COMMENTS = "comments"
    DATE = "date"
    DEFAULT = "default"
    LIKES = "likes"
    MANUAL = "manual"
    PLAYS = "plays"

    __str__ = str.__str__


Sort35OrStr: TypeAlias = Annotated[Sort35 | str, open_enum_validator(Sort35)]
