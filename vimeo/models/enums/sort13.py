from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort13(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    FOLLOWERS = "followers"
    RELEVANT = "relevant"
    VIDEOS = "videos"

    __str__ = str.__str__


Sort13OrStr: TypeAlias = Annotated[Sort13 | str, open_enum_validator(Sort13)]
