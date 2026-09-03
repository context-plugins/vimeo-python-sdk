from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort4(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    FOLLOWERS = "followers"
    VIDEOS = "videos"

    __str__ = str.__str__


Sort4OrStr: TypeAlias = Annotated[Sort4 | str, open_enum_validator(Sort4)]
