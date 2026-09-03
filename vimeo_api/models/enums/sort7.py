from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort7(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    DEFAULT = "default"
    FOLLOWERS = "followers"
    RELEVANT = "relevant"
    VIDEOS = "videos"

    __str__ = str.__str__


Sort7OrStr: TypeAlias = Annotated[Sort7 | str, open_enum_validator(Sort7)]
